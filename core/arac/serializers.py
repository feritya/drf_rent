from arac.models import (
                                        Car,
                                        Bicycle,
                                        Motorcycle,
                                        CarReservation,
                                        Favorite
                                        )

from rest_framework import serializers

from PIL import Image
from  datetime import timedelta  




class CarSerializers(serializers.ModelSerializer):
    class Meta:
        model  =Car
        fields    ='__all__'

class BicycleSerializers(serializers.ModelSerializer):
    class Meta:
        model  =Bicycle
        fields    ='__all__'


class MotorcycleSerializers(serializers.ModelSerializer):
    class Meta:
        model   =Motorcycle
        fields     ='__all__'
        

class CarReservationSerializer(serializers.ModelSerializer):
    rent_per_day      =serializers.IntegerField(source='car.rent_per_day',read_only=True)
    # total_price          = serializers.IntegerField(read_only=True)
    class Meta:
        model    =CarReservation
        fields      = ['customer','car','issue_date','return_date','rent_per_day']

    def validate(self, data):
        price = data.get('rent_per_day')

        if issue_date and return_date:
            issue_date = datetime.strptime(issue_date, '%Y-%m-%d').date()
            return_date = datetime.strptime(return_date, '%Y-%m-%d').date()
            delta = return_date - issue_date
            total_price = price * delta.days
            data['total_price'] = total_price
        
        return data 


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Favorite
        fields     = ('id', 'user', 'content_type', 'object_id')

class CarPastReservationSerializer(serializers.ModelSerializer):
    model                = serializers.CharField(source='car.model',read_only=True)
    rent_per_day      =serializers.IntegerField(source='car.rent_per_day',read_only=True)
    arac_foto_1        = serializers.ImageField(source='car.arac_foto_1',read_only=True)
    total_price      = serializers.IntegerField(read_only=True)

    class Meta:
        model   = CarReservation
        fields     = ('id','model','rent_per_day','arac_foto_1','total_price')
    

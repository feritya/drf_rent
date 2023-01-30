from arac.models import Car,Bicycle,Motorcycle,CarReservation,Favorite
from rest_framework import serializers

class CarSerializers(serializers.ModelSerializer):
    class Meta:
        model =Car
        fields='__all__'

class BicycleSerializers(serializers.ModelSerializer):
    class Meta:
        model =Bicycle
        fields='__all__'


class MotorcycleSerializers(serializers.ModelSerializer):
    class Meta:
        model =Motorcycle
        fields='__all__'

class CarReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model =CarReservation
        fields = '__all__'


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ('id', 'user', 'content_type', 'object_id')







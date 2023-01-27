from arac.models import Car,Bicycle,Motorcycle,CarReservation
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



# class FotoCarSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Car
#         fields =['foto']


# class FotoMototrSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Motorcycle
#         fields =['foto']

# class FotoBicycleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Bicycle
#         fields =['foto']




from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from arac.serializers import BicycleSerializers,MotorcycleSerializers,CarSerializers,CarReservationSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from arac.models import Bicycle,Car,Motorcycle,CarReservation
from rest_framework import permissions
import json
from datetime import date
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view





class MotorcycleAPIView(viewsets.ModelViewSet) :
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class=         MotorcycleSerializers
    queryset =                 Motorcycle.objects.all()



class BicycleAPIView(viewsets.ModelViewSet) :
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class=         BicycleSerializers
    queryset =                 Bicycle.objects.all()



class CarAPIView(viewsets.ModelViewSet) :
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class=         CarSerializers
    queryset =                  Car.objects.all()


class CarReservationAPIView():

    @api_view(['GET'])  #rezervasyonlar gözüküyor 
    def view_all_reservations(request):

        """
        API endpoint for showing all reservations in the system
        .

        Sistemdeki tüm rezervasyonları göstermek için API uç noktası
        """

        if request.method == 'GET':
            reservations = CarReservation.objects.all()
            serializer = CarReservationSerializer(reservations, many=True)
            return Response(serializer.data)


    @api_view(['GET'])  #
    def view_reservation_details(request, rent_pk):
        """
        API endpoint for showing a particular reservation details.
        Belirli bir rezervasyon detayını göstermek için API uç noktası.
        """
        try:
            reservation = CarReservation.objects.get(pk=rent_pk)
        except CarReservation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = CarReservationSerializer(reservation)
            return Response(serializer.data)


    @api_view(['POST'])  #
    def book_car(request):
        """
        API endpoint for booking an available car.
        """
        if request.method == 'POST':
            serializer = CarReservationSerialize(data=request.data)
                
            if serializer.is_valid():
                current_date = date.today()
                issue_date = serializer.validated_data['issue_date']
                return_date = serializer.validated_data['return_date']

                car = serializer.validated_data['car']
                reservations = CarReservation.objects.all().filter(car=car.id)

                # Check if the issue_date of new reservation doesn't clash with any previous reservations
                for r in reservations:
                    if r.issue_date <= issue_date <= r.return_date:
                        content = {"message":"The selected car is not available on this date"}
                        return Response(data=json.dumps(content), status=status.HTTP_400_BAD_REQUEST)

                # Check whether issue_date is not older than today's date, and is less equal to return_date
                if current_date <= issue_date and issue_date <= return_date:
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    @api_view(['DELETE'])
    def cancel_reservation(request, rent_pk):
        """
        API endpoint for cancelling a specific Booking.
        """
        try:
            reservation = CarReservation.objects.get(pk=rent_pk)
        except CarReservation().DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'DELETE':
            reservation.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)



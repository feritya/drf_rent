from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from arac.serializers import( 
                                            BicycleSerializers,
                                            MotorcycleSerializers,
                                            CarSerializers,
                                            CarReservationSerializer,
                                            FavoriteSerializer,
                                            CarPastReservationSerializer,
                                            
)
from rest_framework import viewsets
from rest_framework.response import Response
from arac.models import (
                                        Bicycle,
                                        Car,
                                        Motorcycle,
                                        CarReservation,
                                        Favorite
)
from rest_framework import permissions
import json
from datetime import date
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.contenttypes.models import ContentType
from rest_framework.decorators import api_view



class MotorcycleAPIView(viewsets.ModelViewSet) :
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class           =MotorcycleSerializers
    queryset                    =Motorcycle.objects.all()



class BicycleAPIView(viewsets.ModelViewSet) :
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class           =BicycleSerializers
    queryset                    =Bicycle.objects.all()



class CarAPIView(viewsets.ModelViewSet) :
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class           =CarSerializers
    queryset                    =Car.objects.all()


class PastRezervations(APIView):
    def  get(self, request):
            reservations = CarReservation.objects.all()
            serializer = CarPastReservationSerializer(reservations)
            return Response(serializer.data)



class PastRezervationsDetail(APIView):
    def  get_object(self,pk):
            reservations_instance =get_object_or_404(CarReservation)
            return reservations_instance
    def  get(self, request,pk):
            reservations = CarReservation.objects.all()
            serializer = CarPastReservationSerializer(reservations) 
            return Response(serializer.data)



class FavoriteViewSet(viewsets.ModelViewSet):
    queryset                    = Favorite.objects.all()
    serializer_class           = FavoriteSerializer
    def perform_create(self, serializer):
        content_type = ContentType.objects.get_for_model(self.request.data.get('content_type'))
        serializer.save(user=self.request.user, content_type=content_type, object_id=self.request.data.get('object_id'))





 







































"""
car i??lemleri yap??lacak 
"""

class CarReservationAPIView():

    @api_view(['GET'])  #rezervasyonlar g??z??k??yor 
    def view_all_reservations(request):

        """
        API endpoint for showing all reservations in the system
        .

        Sistemdeki t??m rezervasyonlar?? g??stermek i??in API u?? noktas??
        """

        if request.method == 'GET':
            reservations = CarReservation.objects.all()
            serializer = CarReservationSerializer(reservations, many=True)
            return Response(serializer.data)


    @api_view(['GET'])  #
    def view_reservation_details(request, rent_pk):
        """
        API endpoint for showing a particular reservation details.
        Belirli bir rezervasyon detay??n?? g??stermek i??in API u?? noktas??.
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
            serializer = CarReservationSerializer(data=request.data)
                
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


"""
motosiklet i??lemleri
"""
class CarReservationAPIView():

    @api_view(['GET'])  #rezervasyonlar g??z??k??yor 
    def view_all_reservations(request):

        """
        API endpoint for showing all reservations in the system
        .

        Sistemdeki t??m rezervasyonlar?? g??stermek i??in API u?? noktas??
        """

        if request.method == 'GET':
            reservations = CarReservation.objects.all()
            serializer = CarReservationSerializer(reservations, many=True)
            return Response(serializer.data)


    @api_view(['PUT'])  #
    def view_reservation_details(request, rent_pk):
        """
        API endpoint for showing a particular reservation details.
        Belirli bir rezervasyon detay??n?? g??stermek i??in API u?? noktas??.
        """
        try:
            reservation = CarReservation.objects.get(pk=rent_pk)
        except CarReservation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'PUT':
            serializer = CarReservationSerializer(reservation)
            return Response(serializer.data, status=status.HTTP_201_CREATED)                


    @api_view(['POST'])  #
    def book_car(request):
        """
        API endpoint for booking an available car.
        """
        if request.method == 'POST':
            serializer = CarReservationSerializer(data=request.data)
                
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



from .models import CarReservation

from rest_framework import viewsets

from arac.serializers import CarReservationSerializer,CarPastReservationSerializer
from datetime import date
from rest_framework.response import Response
from rest_framework import status


class CarRezervationsViews(viewsets.ModelViewSet):
    queryset = CarReservation.objects.all()
    serializer_class = CarReservationSerializer
    # permission_classes = [IsAccountAdminOrReadOnly]
    
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        reservations = CarReservation.objects.filter(car=serializer.data['car'])
        issue_date = serializer.data['issue_date']
        return_date = serializer.data['return_date']
        current_date = date.today()
      
        for r in reservations:
            if str(r.issue_date) <= str(issue_date) <= str(r.return_date):
                content = {"message":"The selected car is not available on this date"}
                return Response(content,status=status.HTTP_400_BAD_REQUEST)

        # Check whether issue_date is not older than today's date, and is less equal to return_date
        if str(current_date) <= str(issue_date) and str(issue_date) <= str(return_date):

            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class PastRezData(viewsets.ModelViewSet):
    queryset = CarReservation.objects.all()
    serializer_class = CarPastReservationSerializer


from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from profiller.models import Profil,ProfilDurum
from profiller.api.serializers import ProfilSerializer



#CRUD İŞLEMLERİ

class ProfilList(generics.GenericAPIView):
    queryset =  Profil.objects.all()
    serializer_class =ProfilSerializer
    permission_classes = [IsAuthenticated]



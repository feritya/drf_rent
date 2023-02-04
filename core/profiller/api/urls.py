from django.urls import path
from profiller.api import views

urlpatterns = [
    #profilleri listeleyecek           
    path('kullanici-profilleri/',views.ProfilList.as_view(),name='profil-listesi'),

]
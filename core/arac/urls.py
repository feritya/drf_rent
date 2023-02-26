from django.urls import path, include
from arac.views1 import (
                                        BicycleAPIView,
                                        CarAPIView,
                                        MotorcycleAPIView,
                                        CarReservationAPIView,
                                        FavoriteViewSet,
                                        
                                        PastRezervations,
                                        PastRezervationsDetail
                                        
                                        
)  
from arac.views import  CarRezervationsViews ,PastRezData
from rest_framework.routers import DefaultRouter

from rest_framework import routers


router = routers.DefaultRouter()    
router.register(r'bicycle', BicycleAPIView),
router.register(r'car', CarAPIView),
router.register(r'motorcycle', MotorcycleAPIView),
router.register(r'car_rezervations', CarRezervationsViews ),
router.register(r'favorites', FavoriteViewSet),
router.register(r'pastrez', PastRezData),

urlpatterns =[  
    path('', include(router.urls)),
    path('car/all_rezervations/',CarReservationAPIView.view_all_reservations),
    path('car/add_rezervations/',CarReservationAPIView.book_car),
    path('car/detail_rezervations/<int:rent_pk>',CarReservationAPIView.view_reservation_details),
    path('car/delete_rezervations/<int:rent_pk>',CarReservationAPIView.cancel_reservation),
    path('car/past/',PastRezervations.as_view()),
    path('car/past/<int:rent_pk', PastRezervationsDetail.as_view()),


]+ router.urls
"""

router = DefaultRouter()
router.register(r'car', CarViews,basename="car" )

urlpatterns = router.urls
"""
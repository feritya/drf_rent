from django.urls import path
from arac.views import BicycleAPIView,CarAPIView,MotorcycleAPIView,CarReservationAPIView


from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'bicycle', BicycleAPIView),
router.register(r'car', CarAPIView),
router.register(r'motorcycle', MotorcycleAPIView),
router.register(r'rezervation',CarReservationAPIView)
urlpatterns = router.urls

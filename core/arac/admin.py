from django.contrib import admin
from arac.models import Bicycle,Car,Motorcycle,CarReservation

# Register your models here.
admin.site.register(Bicycle)
admin.site.register(Motorcycle)
admin.site.register(Car)
admin.site.register(CarReservation)
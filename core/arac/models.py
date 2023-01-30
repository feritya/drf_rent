from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey



# Create your models here.


class Car(models.Model):
    car_owner = models.ForeignKey(User, on_delete=models.CASCADE,related_name = 'car' )
    vehicle_number = models.CharField(max_length=20)
    car_location = models.CharField(max_length=20,null=False)
    model = models.CharField(max_length=50)
    seating_capacity = models.IntegerField()
    rent_per_day = models.IntegerField()
    availability = models.BooleanField(null=True)
    about      = models.TextField(max_length=355,null=True, blank=True)
    arac_foto = models.ImageField(null=True,blank=True,upload_to='car_fotolari/%Y/%m/')
    def __str__(self):

            return self.model

            
# class CarImage(models.Model):
#     arac = models.ForeignKey(Car, on_delete=models.CASCADE,related_name='car_img')
#     image =models.ImageField(null=True,blank=True,upload_to='car_fotolari/%Y/%m/')




class Bicycle(models.Model):
    bicycle_owner = models.ForeignKey(User, on_delete=models.CASCADE,related_name = 'bicycle')
    vehicle_number = models.CharField(max_length=20)
    model = models.CharField(max_length=50)
    seating_capacity = models.IntegerField()
    rent_per_day = models.IntegerField()
    availability = models.BooleanField(null=True)
    about      = models.TextField(max_length=355,null=True, blank=True)
    # location= models.GenericIPAddressField()

    def __str__(self):
        return self.model

    # arac_foto = models.ImageField(many =True,null=True,blank=True,upload_to='car_fotolari/%Y/%m/')

class Motorcycle(models.Model):
    motorcycle_owner = models.ForeignKey(User, on_delete=models.CASCADE,related_name = 'motorcycle' )
    vehicle_number = models.CharField(max_length=20)
    model = models.CharField(max_length=50)
    seating_capacity = models.IntegerField()
    rent_per_day = models.IntegerField()
    availability = models.BooleanField(null=True)
    about      = models.TextField(max_length=355,null=True, blank=True)





    def __str__(self):
        return self.model

    # arac_foto = models.ImageField(many =True,null=True,blank=True,upload_to='car_fotolari/%Y/%m/')


#            rezervations rezervasyon               #

class CarReservation(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    issue_date = models.DateField()
    return_date = models.DateField()
    # price = models.IntegerField()
    
    def __str__(self):
        return str(self.customer) + "- " + str(self.car)
    
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')



    



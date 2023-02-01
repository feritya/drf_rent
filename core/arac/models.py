from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.core.validators import MaxValueValidator, MinValueValidator
from profiller.models import MyUser


# Create your models here.


class Car(models.Model):
    car_owner             = models.ForeignKey(MyUser, on_delete=models.CASCADE,related_name = 'car' )
    vehicle_number    = models.CharField(max_length=20)
    car_location          = models.CharField(max_length=20,null=False)
    model                   = models.CharField(max_length=50)
    seating_capacity   =models.PositiveIntegerField(default=4)
    rent_per_day         = models.PositiveIntegerField(  default=99,validators=[MinValueValidator(100)])
    availability             = models.BooleanField(null=True)
    about                    = models.TextField(max_length=355,null=True, blank=True)
    arac_foto_1           = models.ImageField(null=True,blank=True,upload_to='car_fotolari/%Y/%m/')
    arac_foto_2           = models.ImageField(null=True,blank=True,upload_to='car_fotolari/%Y/%m/')
    arac_foto_3           = models.ImageField(null=True,blank=True,upload_to='car_fotolari/%Y/%m/')

    def __str__(self):

            return self.model

class CarReservation(models.Model):
    customer = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    issue_date = models.DateField()
    return_date = models.DateField()
    price = models.IntegerField()
    
    def __str__(self):
        return str(self.customer) + "- " + str(self.car)


class Bicycle(models.Model):
    bicycle_owner = models.ForeignKey(MyUser, on_delete=models.CASCADE,related_name = 'bicycle')    
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
    motorcycle_owner = models.ForeignKey(MyUser, on_delete=models.CASCADE,related_name = 'motorcycle' )
    vehicle_number = models.CharField(max_length=20)
    model = models.CharField(max_length=50)
    seating_capacity = models.IntegerField()
    rent_per_day = models.IntegerField()
    availability = models.BooleanField(null=True)
    about      = models.TextField(max_length=355,null=True, blank=True)
    def __str__(self):
        return self.model


#            rezervations rezervasyon               #


    



class Favorite(models.Model):
    user = models.ForeignKey( MyUser, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    
def __str__(self):
        return self.content_type


    



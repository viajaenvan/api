from django.db import models
from models.models import Model
from brands.models import Brand
from django.conf import settings
import datetime

YEAR_CHOICES = []

for r in range(1980, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r,r))

CAR_CHOICES = [
    (1, 'MINI VAN'),
    (2, 'VAN'),
    (3, 'TECHO ALTO')
]

PASSENGER_CAPACITY_CHOICES = [
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
    (10, '10'),
    (11, '11'),
    (11, '11'),
    (12, '12'),
    (13, '13'),
    (14, '14'),
    (15, '15'),
    (16, '16')
]

CHAIRS_CHOICES = [
    (1, 'INDIVIDUAL'),
    (2, 'COMPLETA'),
    (3, 'RECLINABLE')
]


CHAIRS_CHOICES = [
    (1, 'OSCUROS'),
    (2, 'CLAROS')
]

CARRIER_CHOICES = [
    (1, 'INTERNO'),
    (2, 'EXTERNO')
]


# Create your models here.
class Car(models.Model):
   user =  models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
   license_plate = models.CharField(max_length=10)
   model = models.ForeignKey(Model, on_delete=models.PROTECT)
   brand = models.OneToOneField(Brand, on_delete=models.PROTECT)
   year = models.IntegerField(choices=YEAR_CHOICES, max_length=4)
   kind_of_car = models.IntegerField(choices=CAR_CHOICES, max_length=2)
   passenger_capacity = models.IntegerField(choices=PASSENGER_CAPACITY_CHOICES, max_length=2)
   kind_of_chairs = models.IntegerField(choices=CHAIRS_CHOICES, max_length=2)
   power_suppliers = models.PositiveIntegerField(max_length=3, default=0)
   usb_ports = models.PositiveIntegerField(max_length=3, default=0)
   air_conditioner = models.BooleanField()
   glasses = models.IntegerField(choices=CHAIRS_CHOICES, max_length=2)
   luggage_carrier = models.IntegerField(choices=CARRIER_CHOICES, max_length=2)
   wifi = models.BooleanField()

   def __str__(self):
        return self.license_plate 

   def __unicode__(self):
        return self.license_plate
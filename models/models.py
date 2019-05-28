from django.db import models
from brands.models import Brand
import datetime

YEAR_CHOICES = []

for r in range(1980, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r,r))


# Create your models here.
class Model(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    img = models.ImageField(upload_to='models', null=True, blank=True)
    year = models.IntegerField(choices=YEAR_CHOICES, max_length=4)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

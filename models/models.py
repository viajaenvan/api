from django.db import models
from brands.models import Brand
import datetime

YEAR_CHOICES = ( 
    ('2006', ' 2006'),
    ('2007', ' 2007'),
    ('2008', ' 2008'),
    ('2009', ' 2009'),
    ('2010', ' 2010'),
    ('2011', ' 2011'),
    ('2012', ' 2012'),
    ('2013', ' 2013'),
    ('2014', ' 2014'),
    ('2015', ' 2015'),
    ('2016', ' 2016'),
    ('2017', ' 2017'),
    ('2018', ' 2018'),
    ('2019', ' 2019'),
)


# Create your models here.
class Model(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    img = models.ImageField(upload_to='models')
    year = models.CharField(choices=YEAR_CHOICES, max_length=4)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

from rest_framework import serializers
from .models import Brand

class BrandSerialize(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = Brand
        fields = ('name', 'img_logo', 'create_date')
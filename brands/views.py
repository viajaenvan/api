from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Brand
from .serializers import BrandSerialize


class BradsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows brands to be viewed or edited.
    """
    queryset = Brand.objects.all()
    serializer_class = BrandSerialize
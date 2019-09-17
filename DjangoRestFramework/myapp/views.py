# from django.shortcuts import render
from rest_framework import viewsets

from . import models
from .serializers import CountrySerializer


# ViewSets define the view behavior.
class CountryViewSet(viewsets.ModelViewSet):
    queryset = models.Country.objects.all()
    serializer_class = CountrySerializer

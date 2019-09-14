# from django.shortcuts import render
from rest_framework import viewsets

from . import models
from .serializers import CoordSerializer


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = models.NicePlace.objects.all()
    serializer_class = CoordSerializer

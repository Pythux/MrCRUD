# from django.http import Http404
# from django.shortcuts import get_object_or_404
#
# from rest_framework.response import Response
# from rest_framework.parsers import JSONParser
from rest_framework import generics

from .models import Country
from .serializers import CountrySerializer


class CountryList(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

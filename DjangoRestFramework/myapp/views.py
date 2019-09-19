from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import status
from . import models
from .serializers import CountrySerializer


class CountryList(APIView):
    queryset = models.Country.objects.all()

    def get(self, request, format=None):
        country = models.Country.objects.all()
        serializer = CountrySerializer(country, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CountryDetail(APIView):
    queryset = models.Country.objects.all()

    def get_object(self, pk):
        try:
            return models.Country.objects.get(pk=pk)
        except models.Country.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """Retrieve, update or delete a Country."""
        country = self.get_object(pk)
        serializer = CountrySerializer(country)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        country = get_object_or_404(models.Country, pk=pk)
        data = JSONParser().parse(request)
        serializer = CountrySerializer(country, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        country = get_object_or_404(models.Country, pk=pk)
        country.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

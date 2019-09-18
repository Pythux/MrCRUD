from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from . import models
from .serializers import CountrySerializer


@csrf_exempt
def country_list(request):
    if request.method == 'GET':
        country = models.Country.objects.all()
        serializer = CountrySerializer(country, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CountrySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def country_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        country = models.Country.objects.get(pk=pk)
    except models.Country.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CountrySerializer(country)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CountrySerializer(country, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        country.delete()
        return HttpResponse(status=204)

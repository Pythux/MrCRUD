from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from . import models
from .serializers import CountrySerializer


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def country_list(request, format=None):
    if request.method == 'GET':
        country = models.Country.objects.all()
        serializer = CountrySerializer(country, many=True)
        # return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((permissions.AllowAny,))
def country_detail(request, pk, format=None):
    """Retrieve, update or delete a Country."""
    try:
        country = models.Country.objects.get(pk=pk)
    except models.Country.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = CountrySerializer(country)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CountrySerializer(country, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        country.delete()
        return Response(status=204)

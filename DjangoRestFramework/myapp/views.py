# from django.http import Http404
# from django.shortcuts import get_object_or_404
#
# from rest_framework.response import Response
# from rest_framework.parsers import JSONParser
from rest_framework import generics, permissions

from django.contrib.auth.models import User
from .models import Country
from .serializers import UserSerializer, CountrySerializer
from .permissions import IsOwnerOrReadOnly


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CountryList(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def perform_create(self, serializer):
        """overide instance save"""
        # can give others fields, the "owner" field here
        serializer.save(owner=self.request.user)


class CountryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    # permissions.IsAuthenticatedOrReadOnly not needed, since it is in settings.py
    # at DEFAULT_PERMISSION_CLASSES

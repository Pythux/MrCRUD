
from django.urls import path, include
# from rest_framework import routers
from rest_framework.routers import DefaultRouter
# from rest_framework.urlpatterns import format_suffix_patterns
from . import views


app_name = 'myapp'


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'country', views.CountryViewSet)
router.register(r'user', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
# can't do that now

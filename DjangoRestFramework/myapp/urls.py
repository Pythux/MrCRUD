
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import controller


app_name = 'myapp'


# Create a router and register our controllers with it.
router = DefaultRouter(trailing_slash=False)
router.register(r'user', controller.UserViewSet)
router.register('post', controller.PostViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]

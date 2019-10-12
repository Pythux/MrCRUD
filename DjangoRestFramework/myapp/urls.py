
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import controllers


app_name = 'myapp'

# Create a router and register our controllers with it.
router = DefaultRouter(trailing_slash=False)
router.register(r'user', controllers.UserSet)
router.register('post', controllers.PostSet)
router.register('user_lottie', controllers.UserLottieSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]

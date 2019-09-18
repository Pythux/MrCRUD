
from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


app_name = 'myapp'


# Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'country', views.CountryViewSet)


# Wire up our API using automatic URL routing.
urlpatterns = [
    # path('', include(router.urls)),
    path('country', views.country_list),
    path('country/<int:pk>', views.country_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)

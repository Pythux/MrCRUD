
from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


app_name = 'myapp'


country_list = views.CountryViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
country_detail = views.CountryViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
country_places = views.CountryViewSet.as_view({
        'get': 'places'
})

user_list = views.UserViewSet.as_view({
    'get': 'list'
})
user_detail = views.UserViewSet.as_view({
    'get': 'retrieve'
})

# Wire up our API using automatic URL routing.
urlpatterns = [
    # path('', include(router.urls)),
    path('', views.api_root),
    path('country', country_list, name='country-list'),
    path('country/<int:pk>', country_detail, name='country-detail'),
    path('country/<int:pk>/places', country_places, name='country-detail-places'),
    path('user', user_list, name='user-list'),
    path('user/<int:pk>', user_detail, name='user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

from django.urls import path

from . import views


app_name = 'myapp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('detail/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('list', views.PostListView.as_view(), name='post_list'),
]

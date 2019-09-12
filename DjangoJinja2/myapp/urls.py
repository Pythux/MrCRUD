from django.urls import path

from . import views


app_name = 'myapp'

urlpatterns = [
    path('hello', views.IndexView.as_view(), name='index'),
    path('detail/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('', views.PostListView.as_view(), name='post_list'),
    path('login', views.LoginView.as_view(), name='login')
]

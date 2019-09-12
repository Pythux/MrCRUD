from django.urls import path

from . import views


app_name = 'myapp'


urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('detail/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('update/<int:pk>/', views.PostUpdateView.as_view(), name='post_update'),
    path('delete/<int:pk>/', views.PostDeleteView.as_view(), name='post_delete'),
    path('create', views.PostCreateView.as_view(), name='post_create'),
    path('cards', views.CardsView.as_view(), name='cards')
]

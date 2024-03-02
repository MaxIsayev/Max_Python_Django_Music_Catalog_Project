from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('music/', views.track_list, name='track_list'),
    path('track/<int:pk>/', views.track_detail, name='track_detail'),
]
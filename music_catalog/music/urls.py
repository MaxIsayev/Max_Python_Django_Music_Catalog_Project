from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('music/', views.track_list, name='track_list'),
    path('track/<int:pk>/', views.track_detail, name='track_detail'),
    path('albums/', views.AlbumListView.as_view(), name='album_list'),
    path('album/<int:pk>/', views.AlbumDetailView.as_view(), name='album_detail'),
    path('albums/create/', views.AlbumCreateView.as_view(), name='album_create'),
    path('album/<int:pk>/edit/', views.AlbumUpdateView.as_view(), name='album_update'),
    path('album/<int:pk>/delete/', views.AlbumDeleteView.as_view(), name='album_delete'),

]
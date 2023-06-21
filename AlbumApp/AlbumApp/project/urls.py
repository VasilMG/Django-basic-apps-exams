from django.urls import path

from AlbumApp.project.views import index_view, album_add_view, album_details_view, album_edit_view, album_delete_view, \
    profile_details_view, profile_delete_view

urlpatterns = [
    path('', index_view, name='index'),
    path('album/add/', album_add_view, name='add_album'),
    path('album/details/<int:pk>/', album_details_view, name='album_details'),
    path('album/edit/<int:pk>/', album_edit_view, name='album_edit_view'),
    path('album/delete/<int:pk>/', album_delete_view, name='album_delete_view'),
    path('album/profile/details/', profile_details_view, name='profile_details'),
    path('profile/delete/', profile_delete_view, name='profile_delete'),
]
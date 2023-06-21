from django.urls import path

from Plants.plantsapp.views import index, create_profile, catalogue_view, create_plant_view,\
    plant_details, edit_plant, delete_plant, profile_details, profile_edit, profile_delete

urlpatterns = [
    path('', index, name='index'),
    path('profile/create/', create_profile, name='create_profile' ),
    path('catalogue/', catalogue_view, name='catalogue'),
    path('create/', create_plant_view, name='create_plant'),
    path('details/<int:pk>/', plant_details, name='plant_details'),
    path('edit/<int:pk>/', edit_plant, name='edit_plant'),
    path('delete/<int:pk>/', delete_plant, name='delete_plant'),
    path('profile/details/', profile_details, name='profile_details'),
    path('profile/edit/', profile_edit, name='profile_edit'),
    path('profile/delete/', profile_delete, name='profile_delete'),

]
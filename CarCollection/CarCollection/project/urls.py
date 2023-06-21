from django.urls import path

from CarCollection.project.views import index_view, profile_crete_view, catalogue_view, car_create_view, \
    car_details_view, edit_car_view, delete_car_view, profile_details_view, edit_profile_view, delete_profile_view

urlpatterns = [
    path('', index_view, name='index'),
    path('profile/create', profile_crete_view, name='profile_create'),
    path('catalogue/', catalogue_view, name='catalogue'),
    path('car/creete/', car_create_view, name='car_create'),
    path('car/<int:pk>/details/', car_details_view, name='car_details'),
    path('car/<int:pk>/edit/', edit_car_view, name='edit_car'),
    path('car/<int:pk>/delete/', delete_car_view, name='delete_car'),
    path('car/profile/details/', profile_details_view, name='profile_details'),
    path('car/profile/edit/', edit_profile_view, name='edit_profile'),
    path('car/profile/delete/', delete_profile_view, name='delete_profile'),
]
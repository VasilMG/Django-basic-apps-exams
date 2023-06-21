
from django.contrib import admin
from django.urls import path, include

from Plants import plantsapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("Plants.plantsapp.urls")),
]

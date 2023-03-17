from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import *
from .views import  index

urlpatterns = [
   
    path('', index, name='index'),
    path('add_sensor', add_sensor, name='add_sensor'),
]

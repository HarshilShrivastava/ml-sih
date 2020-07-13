from django.contrib import admin
from django.urls import path,include
from .views import analysis
urlpatterns = [
    path('analysis/', analysis),
   
]
from django.contrib import admin
from django.urls import path,include
from .views import analysis,analysis_api,get_skills
urlpatterns = [
    path('analysis/', analysis),
    path('analysis-get/', analysis_api),
   path('skills-get/', get_skills),
]
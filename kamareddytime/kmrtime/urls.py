from django.contrib import admin
from django.urls import path 
from kmrtime import views

urlpatterns = [
    path('kmrtime',views.kmrtime),
]

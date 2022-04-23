import imp
from django.contrib import admin
from django.urls import path
from chatapp import views

urlpatterns = [
    path('',views.login),
    path('/signup',views.signup),
    path('/login',views.login),
]

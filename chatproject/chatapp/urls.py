import imp
from django.contrib import admin
from django.urls import path
from chatapp import views

urlpatterns = [
    path('',views.chat_page),
    path('signup',views.signup),
    path('login',views.login),
]

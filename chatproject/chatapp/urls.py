import imp
from django.contrib import admin
from django.urls import path
from chatapp import views

urlpatterns = [
    path('login',views.login),
    path('loginvalidation',views.login_validation),
    path('chathomepage',views.chat_homepage),
    path('logout',views.logout),
    path('newmessage',views.new_message),
    path('refresh',views.refresh)
]

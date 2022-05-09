from django.contrib import admin
from django.urls import path 
from restapp import views

urlpatterns = [
    path('',views.start),
    path('name/<str:name>',views.user_name),
    path('p',views.check_post),
    path('telugu',views.translate_to_telugu)
]

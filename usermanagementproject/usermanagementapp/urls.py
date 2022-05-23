from django.contrib import admin
from django.urls import path
from usermanagementapp import views

urlpatterns = [
    path('read',views.read,name= 'read'),
    path('index',views.index,name= 'index'),
    path("adduser", views.adduser, name="adduser"),
    path("deleteuser/<str:line>",views.deleteuser,name='deleteuser'),
    path("edituser/",views.edituser,name= 'edituser')
]

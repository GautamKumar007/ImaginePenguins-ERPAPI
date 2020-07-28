from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from ERPAPI import views

urlpatterns = [
    path('', views.index,name='home'),
    path('api/erpapi/v1/user/register', views.Registration.as_view()),
    path('api/erpapi/v1/user/login', obtain_auth_token),
]
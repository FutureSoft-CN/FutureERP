from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from apps.account import views

urlpatterns = [
    path('',views.login),
    path('login/',views.login),
    path('logout/',views.logout),
]
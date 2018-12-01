from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from apps.account.views import login, logout

urlpatterns = [
    path('',login),
    path('login/',login),
    path('logout/',logout),
]
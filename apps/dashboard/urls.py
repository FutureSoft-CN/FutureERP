from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from apps.dashboard.views import load_dashboard


urlpatterns = [
    path('',load_dashboard),
    path('index/',load_dashboard),
    path('index.html/',load_dashboard),
]
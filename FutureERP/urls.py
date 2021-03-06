"""FutureERP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

from apps.account.views import *
from apps.dashboard.views import load_dashboard

from graphene_django.views import GraphQLView

import xadmin

urlpatterns = [   
    #path('account/', include('account.urls')),
    
    #path('login/',include('account.urls')),
    
#    path('logout/',include('account.urls')),
    
    path('dashboard/',include('dashboard.urls')),
    
#    path('', admin.site.urls),
    path('', xadmin.site.urls),
    
    #path('xadmin/', xadmin.site.urls),
    
    # for test purpose only
    path('direct/', test_redirect),

    url(r'^graphql', GraphQLView.as_view(graphiql=True)),
    
]

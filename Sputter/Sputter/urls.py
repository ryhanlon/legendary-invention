"""Sputter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from sputtNicky.views import (create_sput, read_sput, update_sput, delete_sput, list_sputs)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # create
    url(r'^sput/create/', create_sput, name='home'),
    # read
    url(r'^sput/read/(?P<pk>\d+)/', read_sput, name='home'),
    # update
    url(r'^sput/update/', update_sput, name='home'),
    # delete
    url(r'^sput/delete/', delete_sput, name='home'),
    # list
    url(r'^sput/list/', list_sputs, name='home'),
]

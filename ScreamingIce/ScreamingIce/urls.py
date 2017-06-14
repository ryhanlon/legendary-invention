"""ScreamingIce URL Configuration

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
from inventory.views import scream_maker, scream_taker

from pages.views import home

urlpatterns = [
    # Django Admin
    url(r'^admin/', admin.site.urls),

    # Home Page
    url(r'^$', home, name='home'),

    # Create
    url(r'^ice/create/', scream_maker, name='create'),         # function object, no ()

    # Retrieve
    url(r'^ice/(?P<pk>\d+)', scream_taker, name='retrieve'),
    # Update
    # Delete
]
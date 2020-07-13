"""Inventory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url,include
from MyApp import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home,name = 'home'),
    url(r'^data_entry/$',views.data_entry, name = 'data_entry'),
    url(r'^book_list/$',views.book_list,name = 'book_list'),
    url(r'^book_list/(?P<id>\d+)/$',views.data_edit, name = 'data_edit'),
    url(r'^book_list/(?P<id>\d+)/delete$',views.data_remove, name = 'delete'),
]

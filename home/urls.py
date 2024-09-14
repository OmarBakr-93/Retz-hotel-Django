from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.contrib import admin
from home import views

app_name = 'home'

urlpatterns = [
    path('',views.home, name='home'),
]

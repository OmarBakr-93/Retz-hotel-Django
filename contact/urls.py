from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.contrib import admin
from contact import views

app_name = 'contact'

urlpatterns = [
    path('', views.contact, name='contact'),
]

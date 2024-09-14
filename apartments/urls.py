from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.contrib import admin
from apartments import views

app_name = 'apartments'

urlpatterns = [
    path('', views.apartments),
    path('<apartment_id>', views.apartment, name='apartment'),
]

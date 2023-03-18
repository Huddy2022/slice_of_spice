from django.contrib import admin
from django.urls import path, include
from booking import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('home', views.home, name='home'),
    path('menu', views.menu, name='menu'),
    path('reservations', views.reservations, name='reservations'),
    path('contact', views.contact, name='contact'),
    path('gallery', views.gallery, name='gallery'),
]

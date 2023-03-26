from django.contrib import admin
from django.urls import path, include
from booking import views

urlpatterns = [
    path('', views.index, name='home'),
    path('home', views.home, name='home'),
    path('menu', views.menu, name='menu'),
    path('book_a_table', views.reservations, name='reservations'),
    path('contact', views.contact, name='contact'),
    path('gallery', views.gallery, name='gallery'),
]

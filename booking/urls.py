from django.contrib import admin
from django.urls import path, include
from booking import views

urlpatterns = [
    path('', views.index, name='home'),
    path('home', views.home, name='home'),
    path('menu', views.menu, name='menu'),
    path('book_a_table', views.reservations, name='reservations'),
    path('reservations', views.booked_table, name='booked_table'),
    path('contact', views.contact, name='contact'),
    path('gallery', views.gallery, name='gallery'),
    path('cancel_booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking')
]

from django.contrib import admin
from django.urls import path, include
from booking import views

# Define the URL patterns for booking app
urlpatterns = [
    path('', views.index, name='home'),
    path('home', views.home, name='home'),
    path('menu', views.menu, name='menu'),
    path('book_a_table', views.reservations, name='reservations'),
    path('reservations', views.booked_table, name='booked_table'),
    path('contact', views.contact, name='contact'),
    path('gallery', views.gallery, name='gallery'),
    path('admin/', admin.site.urls, name='admin'),
    # Define the URL pattern for canceling/editing a booking with booking ID
    path('cancel_booking/<int:booking_id>/cancel/',
         views.cancel_booking, name='cancel_booking'),
    path('edit_booking/<int:booking_id>/edit/',
         views.edit_booking, name='edit_booking'),
]

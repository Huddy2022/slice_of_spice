from django.contrib import admin
from django.urls import path, include
from booking import views

urlpatterns = [
    path('', views.index, name='home'),
    path('home', views.home, name='home'),
    path('menu', views.menu, name='menu'),
    path('book_a_table', views.book_a_table, name='book_a_table'),
    path('contact', views.contact, name='contact'),
    path('gallery', views.gallery, name='gallery'),
]

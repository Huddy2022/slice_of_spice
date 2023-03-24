from datetime import datetime

from django.shortcuts import render
from .models import Booking, Cancellation, Table


def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'index.html')


def menu(request):
    return render(request, 'menu.html')


def reservations(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        booking_date = request.POST.get('booking_date')
        booking_time = request.POST.get('booking_time')

        reservations = Booking(name=name, email=email, phone=phone, booking_date=booking_date, booking_time=booking_time)

        reservations.save()

    return render(request, 'reservations.html')


def contact(request):
    return render(request, 'contact.html')


def gallery(request):
    return render(request, 'gallery.html')

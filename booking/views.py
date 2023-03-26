from datetime import datetime

from django.shortcuts import render
from .models import Booking, Cancellation, Table, Customer


def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'index.html')


def menu(request):
    return render(request, 'menu.html')


def reservations(request):
    if request.method == "POST":
        user = request.user
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        booking_date = request.POST.get('date')
        booking_time = request.POST.get('time')
        table = request.POST.get('people')

        reservation = Booking(user=user, booking_date=booking_date, booking_time=booking_time, table_id=table)

        reservation.save()

        return render(request, 'reservations.html')

    return render(request, 'book_a_table.html')


def booked_table(request):
    return render(request, 'reservations.html')


def contact(request):
    return render(request, 'contact.html')


def gallery(request):
    return render(request, 'gallery.html')

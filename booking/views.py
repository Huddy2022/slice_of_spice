from datetime import datetime

from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
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

        customer, created = Customer.objects.get_or_create(user=user)
        customer.email = email
        customer.phone = phone
        customer.save()
        reservation = Booking(customer=customer, booking_date=booking_date, booking_time=booking_time, table_id=table)

        reservation.save()

        messages.success(request, 'Congratulations your table is booked!')

        return render(request, 'book_a_table.html')
        
    return render(request, 'book_a_table.html')


@login_required
def booked_table(request):
    customer = request.user.profile
    return render(request, 'reservations.html', {'customer': customer})


def contact(request):
    return render(request, 'contact.html')


def gallery(request):
    return render(request, 'gallery.html')

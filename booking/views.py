from datetime import datetime

from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
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
        # Retrieve form data
        user = request.user
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        booking_date = request.POST.get('date')
        booking_time = request.POST.get('time')
        table_id = request.POST.get('table')

        # Create or update customer record

        customer, created = Customer.objects.get_or_create(user=user)
        customer.email = email
        customer.phone = phone
        customer.save()

        # Create reservation
        reservation = Booking(customer=customer, booking_date=booking_date, booking_time=booking_time, table_id=table_id)
        reservation.save()

        # Display success message
        messages.success(request, 'Congratulations your table is booked!')

        # Render to home page
        return render(request, 'index.html')

    else:
        # Retrieve available tables
        date = request.GET.get('date')
        time = request.GET.get('time')
        if date is not None and time is not None:
            available_tables = Table.objects.filter(Q(booking__isnull=True) | Q(booking__booking_date__gt=date) | Q(booking__booking_date=date, booking__booking_time__gt=time)).order_by('table_number')
        else:
            available_tables = Table.objects.filter(booking__isnull=True).order_by('table_number')

        # Render the book_a_table template with available tables
        return render(request, 'book_a_table.html', {'available_tables': available_tables})


@login_required
def booked_table(request):
    customer = request.user.profile
    return render(request, 'reservations.html', {'customer': customer})


@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == "POST":
        message = request.POST.get('message')
        cancellation = Cancellation(user=booking, message=message)
        cancellation.save()
        messages.success(request, 'Your cancellation request has been submitted.')
        return render(request, 'index.html')

    return render(request, 'cancel_booking.html', {'booking': booking})


def contact(request):
    return render(request, 'contact.html')


def gallery(request):
    return render(request, 'gallery.html')

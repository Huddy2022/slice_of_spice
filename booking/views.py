from django.shortcuts import render, get_object_or_404
from .models import Booking, Cancellation, Table, Customer
from django.contrib import messages
from django.db.models import Q
from django.utils import timezone
from datetime import timedelta

from django.contrib.auth.decorators import login_required


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
        # num_people = request.POST.get('num_people')

        # Create or update customer record
        customer, created = Customer.objects.get_or_create(user=user)
        customer.email = email
        customer.phone = phone
        customer.save()

        # Create reservation
        table = Table.objects.get(id=table_id)
        reservation = Booking(customer=customer, table=table, booking_date=booking_date, booking_time=booking_time)
        reservation.save()

        # Set the table unavailable for the next hour
        # table = Table.objects.get(id=table_id)
        # table.available = False
        # table.next_available_time = timezone.now() + timedelta(hours=1)
        # table.save()

        # Display success message
        messages.success(request, 'Congratulations your table is booked!')

        # Render to home page
        return render(request, 'index.html')

    # else:
        # Retrieve available tables
        # date = request.GET.get('date')
        # time = request.GET.get('time')
        # if date is not None and time is not None:
            # set tables available that have next available time greater than now
            # tables_to_set_available = Table.objects.filter(available=False, next_available_time__lte=timezone.now())
            # for table in tables_to_set_available:
                # table.available = True
                # table.save()

            # Retrieve available tables that have been available for more than 1 hour
            # available_tables = Table.objects.filter(Q(booking__isnull=True) | Q(booking__booking_date__gt=date) | Q(booking__booking_date=date, booking__booking_time__gt=time)).filter(Q(available=True) | Q(next_available_time__lte=timezone.now())).order_by('table_number')
        # else:
            # Set tables available that have next available time greater than now
            # tables_to_set_available = Table.objects.filter(available=False, next_available_time__lte=timezone.now())
            # for table in tables_to_set_available:
                # table.available = True
                # table.save()

            # available_tables = Table.objects.filter(booking__isnull=True, available=True).order_by('table_number')


        # Render the book_a_table template with available tables
        return render(request, 'book_a_table.html')


    # Retrieve all available tables
    tables = Table.objects.filter(available=True)

    return render(request, 'book_a_table.html', {'Tables': tables})


@login_required
def booked_table(request):
    try:
        customer = request.user.profile
    except Customer.DoesNotExist:
        customer = Customer.objects.create(user=request.user)
        
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

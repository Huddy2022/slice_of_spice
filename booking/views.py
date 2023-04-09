# Import necessary modules
from django.shortcuts import render, get_object_or_404
from .models import Booking, Cancellation, Table, Customer
from django.contrib import messages
from django.db.models import Q
from django.utils import timezone
from datetime import timedelta, datetime

# Import login_required decorator
from django.contrib.auth.decorators import login_required


# Define index view
def index(request):
    return render(request, 'index.html')


# Define home view (which renders the same template as index)
def home(request):
    return render(request, 'index.html')


# Define menu view
def menu(request):
    return render(request, 'menu.html')


# Define reservations view
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

        # Check if the booking date is in the past
        current_date = timezone.now().date()
        booking_datetime = timezone.make_aware(
            datetime.strptime(
                f"{booking_date} {booking_time}", '%Y-%m-%d %H:%M'))
        if booking_datetime < timezone.now():
            messages.error(
                request, f"The selected date '{booking_date}' is in the past."
                         f"Please choose a future date.")
            return render(request, 'book_a_table.html', {
                'Tables': Table.objects.filter(available=True)
            })

        # Create or update customer record
        customer, created = Customer.objects.get_or_create(user=user)
        customer.email = email
        customer.phone = phone
        customer.save()

        # Check if the selected table is already booked for the selected
        # date and time
        existing_reservation = Booking.objects.filter(
            table_id=table_id, booking_date=booking_date,
            booking_time=booking_time).first()

        if existing_reservation:
            # Display an error message and suggest alternative options
            messages.error(request, f'The selected table is already booked on '
                                    f'{booking_date} at {booking_time}. '
                                    f'Please choose a different table, '
                                    f'date or time.')
            return render(request, 'book_a_table.html', {
                'Tables': Table.objects.filter(available=True)})

        # Create reservation
        table = Table.objects.get(id=table_id)
        reservation = Booking(customer=customer, table=table,
                              booking_date=booking_date,
                              booking_time=booking_time)
        reservation.save()

        # Display success message
        messages.success(request, 'Congratulations your table is booked!')

        # Render to home page
        return render(request, 'index.html')

    # Call delete_expired_bookings() function
    delete_expired_bookings()

    # Retrieve all available tables
    tables = Table.objects.filter(available=True)

    return render(request, 'book_a_table.html', {'Tables': tables})


# Define booked_table view where you have to be logged in to book a table
@login_required
def booked_table(request):
    try:
        customer = request.user.profile
    except Customer.DoesNotExist:
        customer = Customer.objects.create(user=request.user)

    return render(request, 'reservations.html', {'customer': customer})


# Define cancel_booking view where you have to be logged in to cancel booking
@login_required
def cancel_booking(request, booking_id):
    # Retrieve booking with specified ID
    booking = get_object_or_404(Booking, id=booking_id)
    # Check if there is an existing cancellation request for the booking
    existing_cancellation = Cancellation.objects.filter(
        user=booking).exists()
    # If form is submitted (POST request)
    if request.method == "POST":
        # If there is an existing cancellation request,
        # display alert message and redirect
        if existing_cancellation:
            messages.warning(
                request,
                'A cancellation request for this booking is already pending.')
            return render(request, 'index.html')
        message = request.POST.get('message')
        # Create a new cancellation request
        cancellation = Cancellation(
            user=booking,
            message=message)
        cancellation.save()
        # Display success message
        messages.success(
            request, 'Your cancellation request has been submitted.')
        return render(request, 'index.html')

    # Render cancel_booking.html with booking data and submitted variable
    return render(request, 'cancel_booking.html', {
        'booking': booking, 'existing_cancellation': existing_cancellation})


# Delete any bookings that have expired on date and time
def delete_expired_bookings():
    # Get current time
    current_time = timezone.now()
    # Filter expired bookings
    expired_bookings = Booking.objects.filter(
        Q(booking_date__lt=current_time.date()) | Q(
            booking_date=current_time.date(),
            booking_time__lte=current_time.time()))
    # Delete expired bookings
    expired_bookings.delete()


# Define contact view
def contact(request):
    return render(request, 'contact.html')


# Define gallery view
def gallery(request):
    return render(request, 'gallery.html')

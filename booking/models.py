from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


# Create a model to represent a Customer
class Customer(models.Model):
    # A one-to-one relationship with the built-in User model in Django
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(max_length=40, blank=True)
    phone = models.CharField(max_length=12, null=True, blank=True)

    def __str__(self):
        return self.user.username


# Create a model to represent a Booking
class Booking(models.Model):
    # A foreign key to the Customer model
    customer = models.ForeignKey(
        'Customer', on_delete=models.CASCADE, related_name='bookings')
    # A foreign key to the Table model
    table = models.ForeignKey('Table', on_delete=models.CASCADE)
    booking_date = models.DateField()
    booking_time = models.TimeField()
    message = models.TextField(max_length=300, null=True, blank=True)

    # Create a unique constraint for the combination of table, date, and time
    class Meta:
        unique_together = ('table', 'booking_date', 'booking_time')

    def __str__(self):
        return f"{self.customer.user.username} - {self.table.table_number}"


# Create a model to represent a Table
class Table(models.Model):
    table_number = models.PositiveIntegerField(unique=True)
    # A field to represent the capacity of the table
    capacity = models.PositiveIntegerField(
        choices=[(i, i) for i in range(1, 5)])
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"Table {self.table_number}"

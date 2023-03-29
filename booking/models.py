from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    email = models.EmailField(max_length=40, blank=True)
    phone = models.CharField(max_length=12, null=True, blank=True)

    def __str__(self):
        return self.user.username


class Booking(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, related_name='bookings')    
    table = models.ForeignKey('Table', on_delete=models.CASCADE)
    booking_date = models.DateField()
    booking_time = models.TimeField()

    class meta:
        unqiue_together = ('table', 'booking_date', 'booking_time')

    def __str__(self):
        return f"{self.customer.user.username} - {self.table.table_number}"


class Table(models.Model):
    table_number = models.PositiveIntegerField(unique=True)
    capacity = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 5)])

    def __int__(self):
        return f"Table {self.table_number}"


class Cancellation(models.Model):
    user = models.ForeignKey('Booking', on_delete=models.CASCADE)
    message = models.TextField(max_length=300, null=True, blank=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Cancellation for {self.user} - Approved: {self.approved}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.approved:
            self.user.delete()

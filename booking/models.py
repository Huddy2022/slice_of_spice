from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=40, blank=True)
    phone = models.CharField(max_length=12, null=True, blank=True)
    reservations = models.ManyToManyField('Booking', blank=True)

    def __str__(self):
        return self.user.username


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)    
    table = models.ForeignKey('Table', on_delete=models.CASCADE)
    booking_date = models.DateField()
    booking_time = models.TimeField()

    def __str__(self):
        return f"{self.user.username} - {self.table.table_number}"


class Table(models.Model):
    number_of_people = models.IntegerField()
    table_number = models.IntegerField(unique=True)

    def __int__(self):
        return self.table_number


class Cancellation(models.Model):
    user = models.ForeignKey('Booking', on_delete=models.CASCADE)
    message = models.TextField(max_length=300, null=True, blank=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.user

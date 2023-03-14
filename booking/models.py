from django.db import models
from cloudinary.models import CloudinaryField


class Customer(models.Model):
    name = models.CharField(max_length=35, null=True, blank=True)
    email = models.EmailField(max_length=40)
    phone = models.IntegerField()

    def __str__(self):
        return self.name


class Booking(models.Model):
    party = models.ForeignKey('Customer', on_delete=models.CASCADE)
    table = models.ForeignKey('Table', on_delete=models.CASCADE)
    booking_date = models.DateField()
    booking_time = models.TimeField()

    def __str__(self):
        return self.party.name


class Table(models.Model):
    number_of_people = models.IntegerField()

    def __int__(self):
        return self.number_of_people


class Cancellation(models.Model):
    user = models.ForeignKey('Customer', on_delete=models.CASCADE)
    message = models.TextField(max_length=300, null=True, blank=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.user

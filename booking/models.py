from django.db import models
from cloudinary.models import CloudinaryField


class Booking(models.Model):
    name = models.CharField(max_length=35, blank=True)
    email = models.EmailField(max_length=40, blank=True)
    phone = models.CharField(max_length=12, null=True, blank=True)
    table = models.ForeignKey('Table', on_delete=models.CASCADE)
    booking_date = models.DateField()
    booking_time = models.TimeField()

    def __str__(self):
        return self.name


class Table(models.Model):
    number_of_people = models.IntegerField()

    def __int__(self):
        return self.number_of_people


class Cancellation(models.Model):
    user = models.ForeignKey('Booking', on_delete=models.CASCADE)
    message = models.TextField(max_length=300, null=True, blank=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.user

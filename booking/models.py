from django.db import models
from cloudinary.models import CloudinaryField


class Booking(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=35)
    subject = models.TextField(default='')
    message = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.name


class Table(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=35)
    date = models.CharField(max_length=200)
    time = models.CharField(max_length=12, default='')
    phone = models.CharField(max_length=30, default='')
    people = models.IntegerField(default='')
    message = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name


class Cancellation(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=35)
    message = models.TextField(max_length=300, null=True, blank=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name

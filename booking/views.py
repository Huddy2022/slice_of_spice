from django.shortcuts import render
from .models import Booking, Table, Cancellation


def say_hello(request):
    table = Table.objects.all()
    return render(request, "templates/index.html")

from django.shortcuts import render
from .models import Customer, Booking, Cancellation, Table


def index(request):
    return render(request, 'index.html')

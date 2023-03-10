from django.shortcuts import render
from .models import Booking, Table, Cancellation


def index(request):
    return render(request, 'index.html')

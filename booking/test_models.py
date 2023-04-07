from django.test import TestCase
from django.contrib.auth.models import User
from .models import Customer, Booking, Table, Cancellation
from datetime import date, time


class ModelsTest(TestCase):
    def setUp(self):
        # Create a user to use in the tests
        self.user = User.objects.create_user(
            username='testuser', password='testpass')
        # Create a customer linked to the user
        self.customer = Customer.objects.create(user=self.user)
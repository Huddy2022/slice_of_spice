from django.test import TestCase
from django.contrib.auth.models import User
from .models import Customer, Booking, Table
from datetime import date, time


class ModelsTest(TestCase):
    def setUp(self):
        # Create a user to use in the tests
        self.user = User.objects.create_user(
            username='testuser', password='testpass')
        # Create a customer linked to the user
        self.customer = Customer.objects.create(user=self.user)

    def test_customer_str(self):
        # Test the __str__ method of the Customer model
        self.assertEqual(str(self.customer), 'testuser')

    def test_table_str(self):
        # Test the __str__ method of the Table model
        table = Table.objects.create(table_number=1, capacity=2)
        self.assertEqual(str(table), 'Table 1')

    def test_booking_str(self):
        # Test the __str__ method of the Booking model
        table = Table.objects.create(table_number=1, capacity=2)
        booking = Booking.objects.create(
            customer=self.customer, table=table,
            booking_date=date.today(), booking_time=time(hour=14, minute=30))
        self.assertEqual(str(booking), 'testuser - 1')

    def test_booking_unique_together(self):
        # Test that the unique_together constraint is
        # working in the Booking model
        table = Table.objects.create(table_number=1, capacity=2)
        booking1 = Booking.objects.create(
            customer=self.customer, table=table, booking_date=date.today(),
            booking_time=time(hour=14, minute=30))
        with self.assertRaises(Exception):
            booking2 = Booking.objects.create(
                customer=self.customer, table=table, booking_date=date.today(),
                booking_time=time(hour=14, minute=30))

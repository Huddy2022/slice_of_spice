from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, timedelta
from django.utils import timezone
from .models import Table, Booking, Customer, Cancellation
from booking.views import delete_expired_bookings


# Create your tests here.
class TestViews(TestCase):

    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(
            username='testuser', email='testuser@example.com',
            password='testpass')
        # Create a customer associated with the user
        self.customer = Customer.objects.create(user=self.user)
        # Create a table
        self.table = Table.objects.create(table_number=1, capacity=2)
        # Create a booking associated with the customer and table
        self.booking = Booking.objects.create(
            customer=self.customer, table=self.table,
            booking_date='2023-04-28', booking_time='12:00')
        # URL for cancel_booking view
        self.url = reverse('cancel_booking', args=[self.booking.id])

    # test the index view
    def test_index_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    # test the book_a_table view
    def test_book_a_table_view(self):
        response = self.client.get('/book_a_table')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_a_table.html')

    # test the menu view
    def test_menu_view(self):
        response = self.client.get('/menu')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu.html')

    # test the gallery view
    def test_gallery_view(self):
        response = self.client.get('/gallery')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gallery.html')

    # test the reservations view (GET request)
    def test_reservations_view_get(self):
        # authenticate client as user
        self.client.login(username='testuser', password='testpass')
        response = self.client.get('/reservations')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reservations.html')

    # test the reservations view (POST request)
    def test_reservations_view_post(self):
        data = {
            'name': 'Test User',
            'email': 'testuser@example.com',
            'phone': '1234567890',
            'date': datetime.now() + timedelta(days=2),
            'time': '20:00',
            'table': self.table.id
        }
        self.client.force_login(self.user)
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertTrue(Booking.objects.filter(
            customer=self.customer).exists())

    # test the cancel_booking view (GET request)
    def test_cancel_booking_view_get(self):
        # Log in as the user
        self.client.force_login(self.user)
        # Issue a GET request to the cancel_booking view
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cancel_booking.html')
        # Check that the booking table is displayed in the template
        self.assertContains(response, self.booking.table)

    # test the cancel_booking view (POST request)
    def test_cancel_booking_view_post(self):
        self.client.force_login(self.user)
        data = {
            'message': 'I need to cancel my booking.'
        }
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertTrue(Cancellation.objects.filter(
            user=self.booking).exists())

    # test the delete_expired_booking view
    def test_delete_expired_bookings(self):
        # Create a customer associated with a user
        user = User.objects.create_user(
            username='testuser2', email='testuser@example.com',
            password='testpass')
        customer = Customer.objects.create(user=user)
        # Create a table Id
        table = Table.objects.create(table_number=2, capacity=2)
        # Create a booking in the past associated with the customer
        past_booking = Booking.objects.create(
            customer=customer,
            table_id=table.id,
            booking_date=timezone.now().date() - timezone.timedelta(days=1),
            booking_time=timezone.now().time()
        )
        # Create a booking in the future associated with the customer
        future_booking = Booking.objects.create(
            customer=customer,
            table_id=table.id,
            booking_date=timezone.now().date() + timezone.timedelta(days=1),
            booking_time=timezone.now().time()
        )
        # Call the delete_expired_bookings function
        delete_expired_bookings()
        # Check that the past booking was deleted
        self.assertFalse(Booking.objects.filter(pk=past_booking.pk).exists())
        # Check that the future booking was not deleted
        self.assertTrue(Booking.objects.filter(pk=future_booking.pk).exists())
        # Check that the customer was not deleted
        self.assertTrue(Customer.objects.filter(pk=customer.pk).exists())

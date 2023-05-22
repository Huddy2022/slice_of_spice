from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, timedelta
from django.utils import timezone
from .models import Table, Booking, Customer
from booking.views import delete_expired_bookings
from django.contrib.messages import get_messages


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
            booking_date='2023-06-28', booking_time='12:00')
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
            'date': datetime.now().date() + timedelta(days=2),
            'time': '20:00',
            'table': self.table.id
        }
        self.client.force_login(self.user)
        response = self.client.post('/reservations', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reservations.html')
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
        # Log in as the user
        self.client.force_login(self.user)
        # Issue a GET request to the cancel_booking view
        response = self.client.post(self.url)
        # Check that the booking is deleted
        self.assertFalse(Booking.objects.filter(pk=self.booking.pk).exists())
        # Check for success message in messages
        messages = [str(msg) for msg in response.context['messages']]
        self.assertIn('Your cancellation has been successful.', messages)
        # Check that the response renders the index.html template
        self.assertTemplateUsed(response, 'index.html')

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

    # test the edit_booking view (Post request)
    def test_edit_booking_view_post(self):
        # Log in as the user
        self.client.force_login(self.user)
        # Update the customer data
        self.customer.name = 'New Name'
        self.customer.email = 'newemail@example.com'
        self.customer.phone = '1234567890'
        self.customer.save()
        # Update the booking date
        self.booking.booking_date = '2023-06-30'
        self.booking.booking_time = '15:00'
        self.booking.message = 'New message'
        self.booking.save()
        # Define the new data for the booking
        new_data = {
            'name': self.customer.name,
            'email': self.customer.email,
            'phone':  self.customer.phone,
            'date': '2023-06-30',
            'time': '15:00',
            'table': self.table.id,
            'message': 'New message',
        }
        # Generate the URL for the edit_booking view
        edit_booking_url = reverse('edit_booking', args=[self.booking.id])
        # Issue a POST request to the edit_booking view
        response = self.client.post(edit_booking_url, data=new_data)
        # Refresh the booking instance from the database
        self.booking.refresh_from_db()
        # Check that the booking data has been updated
        self.assertEqual(self.booking.customer.name, 'New Name')
        self.assertEqual(self.booking.customer.email, 'newemail@example.com')
        self.assertEqual(self.booking.customer.phone, '1234567890')
        self.assertEqual(str(self.booking.booking_date), '2023-06-30')
        self.assertEqual(str(self.booking.booking_time), '15:00:00')
        self.assertEqual(self.booking.table.id, self.table.id)
        self.assertEqual(self.booking.message, 'New message')
        # Check that the response renders the index.html template
        self.assertTemplateUsed(response, 'index.html')

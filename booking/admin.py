from django.contrib import admin
from .models import Booking, Table, Customer


# Registering the Customer model with the admin site
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    search_fields = ['user_username', 'name', 'phone']
    list_filter = ('user', 'phone')


# Registering the Booking model with the admin site
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('customer', 'table', 'booking_date', 'booking_time',
                    'message')
    search_fields = ['customer', 'booking_date']
    list_filter = ('customer', 'booking_date')


# Registering the Table model with the admin site
@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    search_fields = ['number_of_people']


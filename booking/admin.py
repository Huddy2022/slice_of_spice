from django.contrib import admin
from .models import Booking, Table, Cancellation, Customer


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


# Registering the Cancellation model with the admin site
@admin.register(Cancellation)
class CancellationAdmin(admin.ModelAdmin):
    list_display = ('user', 'approved')
    search_fields = ['user', 'approved']
    list_filter = ('user', 'approved')
    actions = ['approve_cancellation']

    # Define approve_cancellation action to approve selected cancellations
    def approve_cancellation(self, request, queryset):
        queryset.update(approved=True)

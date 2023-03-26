from django.contrib import admin
from .models import Booking, Table, Cancellation, Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    search_fields = ['user_username', 'phone']
    list_filter = ('user', 'phone')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('customer', 'table', 'booking_date')
    search_fields = ['customer', 'booking_date']
    list_filter = ('customer', 'booking_date')


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    search_fields = ['number_of_people']


@admin.register(Cancellation)
class CancellationAdmin(admin.ModelAdmin):
    list_display = ('user', 'approved')
    search_fields = ['user', 'approved']
    list_filter = ('user', 'approved')
    actions = ['approve_cancellation']

    def approve_cancellation(self, request, queryset):
        queryset.update(approved=True)

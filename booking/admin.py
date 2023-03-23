from django.contrib import admin
from .models import Customer, Booking, Table, Cancellation


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ['name', 'phone']
    list_filter = ('name', 'phone')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('party', 'table', 'booking_date')
    search_fields = ['party', 'booking_date']
    list_filter = ('party', 'booking_date')


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

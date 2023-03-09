from django.contrib import admin
from .models import Booking, Table, Cancellation


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date')
    search_fields = ['name', 'date']
    list_filter = ('name', 'date')


@admin.register(Table)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date')
    search_fields = ['name', 'date']
    list_filter = ('name', 'date')


@admin.register(Cancellation)
class CancellationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ['name', 'email']
    list_filter = ('name', 'email')
    actions = ['approve_cancellation']

    def approve_cancellation(self, request, queryset):
        queryset.update(approved=True)

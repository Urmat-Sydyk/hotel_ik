from django.contrib import admin

# Register your models here.
from backend.apps.booking.models import Rooms, Booking


@admin.register(Rooms)
class AllUsersAdmin(admin.ModelAdmin):
    list_display = [
        'type',
        'number'
    ]
    ordering = ['number']


@admin.register(Booking)
class AllUsersAdmin(admin.ModelAdmin):
    list_display = [
        'guest_name',
        'room_id',
        'check_in',
        'check_out',
        'status',
        'creater'
    ]
    ordering = ['room_id', 'check_in']
    list_editable = ['room_id', 'check_in', 'check_out', 'status']

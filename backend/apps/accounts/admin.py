from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from backend.apps.accounts.models import User


@admin.register(User)
class AllUsersAdmin(UserAdmin):
    list_display = [
        'pin',
        'first_name',
        'middle_name',
        'mobile',
        'is_active'
    ]
    list_editable = ['is_active']
    add_fieldsets = (
        (None, {'fields': ('pin', 'first_name', 'middle_name',  'last_name', 'avatar', 'is_active', 'mobile', 'password1', 'password2'), }),
    )
    fieldsets = (
        (None, {'fields': ('pin', 'first_name', 'middle_name',  'last_name', 'avatar', 'is_active', 'mobile', 'password'), }),
    )
    ordering = ['-id']

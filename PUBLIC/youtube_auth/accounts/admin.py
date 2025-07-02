from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class CustomUserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'is_active', 'is_staff', 'date_joined')
    search_fields = ('username', 'email')
    ordering = ('-date_joined',)
    list_filter = ('is_active', 'is_staff', 'date_joined')
    fieldsets = (
        ('User Info', {
            'fields': ('username', 'email', 'password')
        }),  
    )

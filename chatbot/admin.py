from django.contrib import admin
from .models import Customer, Appointment

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'instagram_handle', 'phone')
    search_fields = ('name', 'email', 'instagram_handle', 'phone')
    list_filter = ('name',)
    ordering = ('name',)
    list_per_page = 10

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('customer', 'service', 'date', 'status')
    search_fields = ('customer__name', 'service')
    list_filter = ('status',)
    ordering = ('date',)
    list_per_page = 10

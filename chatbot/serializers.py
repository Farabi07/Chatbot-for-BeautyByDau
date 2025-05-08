from rest_framework import serializers
from .models import Customer, Appointment

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'email', 'instagram_handle', 'phone']

class AppointmentSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)

    class Meta:
        model = Appointment
        fields = ['id', 'customer', 'service', 'date', 'status']

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Appointment, Customer
from .serializers import AppointmentSerializer

# Book an appointment
@api_view(['POST'])
def book_appointment(request):
    if request.method == 'POST':
        customer_id = request.data.get('customer_id')
        service = request.data.get('service')
        date = request.data.get('date')
        
        customer = Customer.objects.get(id=customer_id)
        appointment = Appointment.objects.create(
            customer=customer,
            service=service,
            date=date,
            status='booked'
        )
        
        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# Cancel an appointment
@api_view(['DELETE'])
def cancel_appointment(request, appointment_id):
    try:
        appointment = Appointment.objects.get(id=appointment_id)
        appointment.status = 'cancelled'
        appointment.save()
        
        return Response({"message": "Appointment cancelled successfully."}, status=status.HTTP_200_OK)
    except Appointment.DoesNotExist:
        return Response({"error": "Appointment not found."}, status=status.HTTP_404_NOT_FOUND)

# List appointments
@api_view(['GET'])
def list_appointments(request):
    appointments = Appointment.objects.all()
    serializer = AppointmentSerializer(appointments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

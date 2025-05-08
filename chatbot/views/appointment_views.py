from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from chatbot.models import Appointment, Customer
from chatbot.serializers import AppointmentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication

# Book an appointment (Requires Authentication)
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def book_appointment(request):
    customer_id = request.data.get('customer_id')
    service = request.data.get('service')
    date = request.data.get('date')

    try:
        customer = Customer.objects.get(id=customer_id)
    except Customer.DoesNotExist:
        return Response({"error": "Customer not found."}, status=status.HTTP_404_NOT_FOUND)

    appointment = Appointment.objects.create(
        customer=customer,
        service=service,
        date=date,
        status='booked'
    )

    serializer = AppointmentSerializer(appointment)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

# Cancel an appointment (Requires Authentication)
@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
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

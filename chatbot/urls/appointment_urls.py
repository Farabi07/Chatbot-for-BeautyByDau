
from django.urls import path
from ..views.appointment_views import book_appointment, cancel_appointment, list_appointments

urlpatterns = [
    path('book/', book_appointment),
    path('cancel/<int:appointment_id>/', cancel_appointment),
    path('list/', list_appointments),
]

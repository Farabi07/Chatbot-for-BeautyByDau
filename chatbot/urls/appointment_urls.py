from django.urls import path
from chatbot.views import appointment_views as views

urlpatterns = [
    path('appointments/', views.book_appointment),
    path('appointments/<int:appointment_id>/cancel/', views.cancel_appointment),
    path('appointments_list/', views.list_appointments,),
]

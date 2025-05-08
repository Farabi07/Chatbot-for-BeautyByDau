from django.urls import path
from . import views

urlpatterns = [
    path('appointments/', views.book_appointment),
    path('appointments/<int:appointment_id>/cancel/', views.cancel_appointment),
    path('appointments/', views.list_appointments),
]

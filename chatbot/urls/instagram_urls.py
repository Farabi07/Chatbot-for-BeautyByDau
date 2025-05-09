from chatbot.views import instagram_views as views
from django.urls import path

urlpatterns = [
    # Instagram webhook URL
    path('instagram/webhook/', views.instagram_webhook),
]
from chatbot.views import shopify_views as views
from django.urls import path

urlpatterns = [
    # Shopify webhook URL
    path('shopify/webhook/', views.chatbot_response),
]
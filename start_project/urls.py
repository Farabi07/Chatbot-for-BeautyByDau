from django.urls import path, include

urlpatterns = [
    path('appointments/', include('chatbot.urls.appointment_urls')),  # Redirects to appointment URLs
    path('instagram/', include('chatbot.urls.instagram_urls')),      # Instagram related URLs
    path('shopify/', include('chatbot.urls.shopify_urls')),          # Shopify related URLs
    path('users/', include('chatbot.urls.user_urls')),               # User management URLs
]


from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('chatbot.urls.user_urls')),
    path('api/', include('chatbot.urls.appointment_urls')),
    path('api/', include('chatbot.urls.shopify_urls')),
    path('api/', include('chatbot.urls.instagram_urls')),
    # path('api/', include('chatbot.urls.customer_urls')),
    # path('api/', include('chatbot.urls.service_urls')),



]

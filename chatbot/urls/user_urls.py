from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from chatbot.views import users_views as views

urlpatterns = [
    # User registration
    path('register/', views.register_user),
    
    # JWT Token endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
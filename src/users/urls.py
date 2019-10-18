# Django
from django.urls import path, include

# Viewsets
from .viewsets import (
    UserRegistrationAPIView, 
    RetrieveUpdatePreferedLanguageAPIView,
    test_access_token
)

# Simple JWT
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'users'

urlpatterns = [
    path('signup/', UserRegistrationAPIView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path(
        'prefered-language/', 
        RetrieveUpdatePreferedLanguageAPIView.as_view(), 
        name='set_prefered_language'
    ),

    path(
        'token/test-access-token/',
        test_access_token,
        name='test_access_token'
    ),
    
]
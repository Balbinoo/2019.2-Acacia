from django.urls import path
from .viewsets import (
    UserRegistrationAPIView,
    RetrieveUpdatePreferedLanguageAPIView,
    test_access_token,
    ProfileUpdateAPIView,
    CreateAccessToken,
    RefreshAccessToken,
)


app_name = 'users'

urlpatterns = [
    path(
        'signup/',
        UserRegistrationAPIView.as_view(),
        name='register'
    ),
    path(
        'signup',
        UserRegistrationAPIView.as_view(),
        name='register'
    ),
    path(
        'token/',
        CreateAccessToken.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'token',
        CreateAccessToken.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'token/refresh/',
        RefreshAccessToken.as_view(),
        name='token_refresh'
    ),
    path(
        'token/refresh',
        RefreshAccessToken.as_view(),
        name='token_refresh'
    ),
    path(
        'prefered-language/',
        RetrieveUpdatePreferedLanguageAPIView.as_view(),
        name='set_prefered_language'
    ),
    path(
        'prefered-language',
        RetrieveUpdatePreferedLanguageAPIView.as_view(),
        name='set_prefered_language'
    ),
    path(
        'token/test-access-token/',
        test_access_token,
        name='test_access_token'
    ),
    path(
        'token/test-access-token',
        test_access_token,
        name='test_access_token'
    ),
    path(
        'profile/',
        ProfileUpdateAPIView.as_view(),
        name='profile_update'
    ),
]

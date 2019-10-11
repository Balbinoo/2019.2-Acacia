
# Django Rest Framework
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.authtoken.models import Token

# Models
from .models import User, Profile

# Serializers
from .serializers import UserSignUpSerializer, ProfileModelSerializer


class UserRegistrationAPIView(CreateAPIView):
    """
    Endpoint for user registration
    """

    permission_classes = (permissions.AllowAny, )
    serializer_class = UserSignUpSerializer
    queryset = User.objects.all()

class ProfileUpdateAPIView(UpdateAPIView):
    """
    Endpoint for user registration
    """

    permission_classes = (permissions.AllowAny, )
    serializer_class = ProfileModelSerializer
    queryset = Profile.objects.all()
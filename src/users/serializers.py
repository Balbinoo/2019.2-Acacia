from .models import User
from rest_framework import serializers
from django.conf import settings

class UserRegistrationSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        required=True,
        label="Email Address"
    )

    password = serializers.CharField(
        write_only=True,
        required=True,
        label="Password",
        style={'input_type': 'password'}
    )

    confirm_password = serializers.CharField(
        write_only=True,
        required=True,
        label="Confirm Password",
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']

    def validade_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Email already exists.')
        return email


    def validate_password(self, password):
        min_length = getattr(settings, 'PASSWORD_MIN_LENGTH', 8)
        if len(password) < min_length:
            raise serializers.ValidationError(
                'Password should be atleast %s characters long.' % (min_length)
            )
        return password

    def validate_confirm_password(self, password_confirmation):
        data = self.get_initial()
        password = data.get('password')
        if password != password_confirmation:
            raise serializers.ValidationError('Passwords must match.')
        return password_confirmation

    def validate_username(self, username):
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError('Email already exists.')
        return username

    def create(self, validated_data):
        del validated_data["confirm_password"]
        return super(UserRegistrationSerializer, self).create(validated_data)

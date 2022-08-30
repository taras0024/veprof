from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class SignInSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')

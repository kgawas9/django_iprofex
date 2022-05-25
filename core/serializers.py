from unittest.util import _MAX_LENGTH
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer

from rest_framework import serializers

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        is_verified = serializers.BooleanField(read_only=True)

        fields = [
            'id','username','password','email','first_name','last_name','is_verified'
        ]


class AccountVerifySerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)


class ResendOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()
    
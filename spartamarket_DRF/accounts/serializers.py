from rest_framework import serializers
from .models import User

class AccountSignInSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "nickname",
            "password",
            "email",
            "birthday",
            "self_introduction",
            "gender"
        )

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        exclude = [
            "is_superuser",
            "password",
            "last_login",
            "groups",
            "user_permissions"
        ]
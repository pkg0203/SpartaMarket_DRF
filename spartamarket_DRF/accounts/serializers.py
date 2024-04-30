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
        model = User
        exclude = [
            "is_superuser",
            "password",
            "last_login",
            "groups",
            "user_permissions"
        ]

#이메일, 이름, 닉네임, 생일 입력 필요하며, 성별, 자기소개
class UserProfileUpdateSerializer(UserProfileSerializer):
    class Meta:
        model = User
        fields=[
            'email',
            'username',
            'nickname',
            'birthday',
            'gender',
            'self_introduction',
        ]
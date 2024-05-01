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
    following = serializers.IntegerField(source="follow.count", read_only=True)
    follower = serializers.IntegerField(source="follower.count", read_only=True)
    class Meta:
        model = User
        fields=[
            'id',
            'username',
            'email',
            'nickname',
            'gender',
            'birthday',
            'self_introduction',
            'following',
            'follower'
        ]

#이메일, 이름, 닉네임, 생일 입력 필요하며, 성별, 자기소개
class UserProfileUpdateSerializer(UserProfileSerializer):
    class Meta(UserProfileSerializer.Meta):
        fields = [
            'username',
            'email',
            'nickname',
            'gender',
            'birthday',
            'self_introduction'
        ]

class UserPasswordUpdateSerializer(UserProfileSerializer):
    class Meta(UserProfileSerializer.Meta):
        fields = [
            'password'
        ]
        
from rest_framework import serializers
from .models import User

class AccountSignInSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username"
        )
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import *
# Create your views here.


class AccountSignInView(APIView):
    def post(self, request):
        serializer = AccountSignInSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            user.set_password(request.data["password"])
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class AccountDetailView(APIView):
    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request, user_pk):
        user = get_object_or_404(User, pk=user_pk)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)

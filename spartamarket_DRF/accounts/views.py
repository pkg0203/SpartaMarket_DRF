from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *
# Create your views here.
class AccountSignIn(APIView):
    def post(self, request):
        serializer = AccountSignInSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save() 
            user.set_password(request.data["password"])  
            user.save()  
            return Response(serializer.data, status=status.HTTP_201_CREATED)

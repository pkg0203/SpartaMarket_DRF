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
        
    def delete(self,request):
        if request.user.is_authenticated:
            print(request.data)
            if request.user.check_password(request.data["password"]):
                request.user.delete()
                data = {f"{request.user.username} is successfully deleted."}
                return Response(data,status=status.HTTP_200_OK)
            return Response({"비밀번호가 틀렸습니다."},status=status.HTTP_400_BAD_REQUEST)
        return Response({"로그인을 해주세요."},status=status.HTTP_401_UNAUTHORIZED)


class AccountDetailView(APIView):
    # permission_classes = [
    #     IsAuthenticated
    # ]
    def get_user(self,username):
        return get_object_or_404(User, username=username)
    
    def get(self, request, username):
        serializer = UserProfileSerializer(self.get_user(username))
        return Response(serializer.data)
    
    def put(self,request,username):
        user=self.get_user(username)
        if user == request.user:
            serializer = UserProfileUpdateSerializer(user,data=request.data,partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        return Response({"본인만 수정할 수 있습니다. 또는 로그인하지 않았습니다."},status=status.HTTP_401_UNAUTHORIZED)

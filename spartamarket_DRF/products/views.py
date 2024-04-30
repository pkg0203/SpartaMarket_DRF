from django.shortcuts import render,get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response 
from .serializers import *

# Create your views here.
class ProductsView(APIView):
    def get(self,request):
        products=Product.objects.all()
        serializer= ProductSerializer(products,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
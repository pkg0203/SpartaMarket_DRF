from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *

# Create your views here.


class ProductsView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        if request.user.is_authenticated:
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(author=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class ProductsDetailView(APIView):
    def delete(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        if request.user.is_authenticated:
            if request.user == product.author:
                product.delete()
                data = {f"pk : {product_id} is successfully deleted"}
                return Response(data, status=status.HTTP_200_OK)
            return Response({"본인의 글이 아닙니다."},status=status.HTTP_403_FORBIDDEN)
        return Response({"로그인을 해주세요."},status=status.HTTP_401_UNAUTHORIZED)

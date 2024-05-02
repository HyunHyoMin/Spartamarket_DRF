from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from .models import Product
from .serializers import ProductSerializer


class ProductList(APIView):
    permission_classes = [IsAuthenticated]
    paginator = PageNumberPagination()

    def get(self, request):
        products = Product.objects.all()
        result_page = self.paginator.paginate_queryset(products, request)
        serializer = ProductSerializer(result_page, many=True)
        return self.paginator.get_paginated_response(serializer.data)
    
    def post(self, request):
        serializer = ProductSerializer(data=request.data, context={"request":request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)
    
    def put(self, request, productId):
        product = get_object_or_404(Product, pk=productId)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, productId):
        product = get_object_or_404(Product, pk=productId)
        product.delete()
        return Response({"message" : "product delete success"})
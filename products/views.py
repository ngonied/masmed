from django.shortcuts import render
from rest_framework import generics,  status, permissions
from rest_framework.views import APIView
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response as MyResponse



class AllProductsListView(generics.ListAPIView):
    queryset = Product.objects.filter(available = True)
    serializer_class = ProductSerializer


class AllCategoriesListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductDetailView(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request, slug):
        
        queryset = get_object_or_404(Product, slug = slug)
        serializer = ProductSerializer(queryset, context={"request": request})
        return MyResponse(serializer.data, status=status.HTTP_200_OK )





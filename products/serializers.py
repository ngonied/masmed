from .models import Product, Category
from rest_framework import serializers







class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name','description', 'manufacturer', 'price', 'quantityInProduct','quantityInStock', 'image', 'seller', 'category', 'overTheCounter']



class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only = True)
    class Meta:
        model = Category
        fields = ['name', 'description', 'products']

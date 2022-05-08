from .models import Product, Category
from rest_framework import serializers



class CategorySerializer(serializer.ModelSerializer):
    class Meta:
        fields = ['name', 'description']




class Product(serializer.ModelSerializer):
    class Meta:
        fields = ['name','description', 'manufacturer', 'price', 'quantityInProduct','quantityInStock', 'image', 'seller', 'category', 'overTheCounter']
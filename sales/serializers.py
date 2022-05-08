from rest_framework import serializers
from .models import Order, OrderItems



class OrderSerializer(serializer.ModelSerializer):
    class Meta:
        fields = '__all__'




class OrderItemsSerializer(serializer.ModelSerializer):
    class Meta:
        fields = '__all__'
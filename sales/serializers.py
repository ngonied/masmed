from rest_framework import serializers
from .models import Order, OrderItems, Cart, CartItem



class OrderSerializer(serializer.ModelSerializer):
    class Meta:
        fields = '__all__'




class OrderItemsSerializer(serializer.ModelSerializer):
    class Meta:
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    class Meta:
        model = Cart
        fields = ['customer', 'cart_id', 'pescription', 'paid', 'date', 'pay_on_delivery', 'items']
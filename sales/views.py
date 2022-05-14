from django.shortcuts import render
from rest_framework.views import APIView
from cart.cart import Cart
from .models import Order, OrderItem
from .serializers import OrderSerializer
from rest_framework import status, permissions
from rest_framework.response import Response


class CreateOrder(APIView):
    permission_classes = (permissions.AllowAny, )
    def post(self, request):
        cart = Cart(request)
        serializer = OrderSerializer(data = request.data)
        if serializer.is_valid():
            order = serializer.save()
            print("saved")
            for item in cart:
                OrderItem.objects.create(order =order,
                product = item['product'],
                price = item['price'],
                quantity = item['quantity'])
            
            order.total_price = int(cart.get_total_price())
            order.save()
            

            cart.clear()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else: 
            return Response(serializer.errors)
        

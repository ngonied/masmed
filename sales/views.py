from django.shortcuts import render
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from cart.cart import Cart
from .models import Order, OrderItem
from .serializers import OrderSerializer
from rest_framework import status, permissions
from rest_framework.response import Response
from .tasks import order_created
from django.db.models.signals import post_save
from django.core.mail import send_mail



class CreateOrder(APIView):
    permission_classes = (permissions.AllowAny, )
    def post(self, request):
        cart = Cart(request)
        serializer = OrderSerializer(data = request.data)
        if serializer.is_valid():
            order = serializer.save()
            
            for item in cart:
                OrderItem.objects.create(order =order,
                product = item['product'],
                price = item['price'],
                quantity = item['quantity'])
            
            order.total_price = int(cart.get_total_price())
            order.save()
            #sentMail(order.id, cart)

            cart.clear()
            order_created.delay(order.id)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else: 
            return Response(serializer.errors)


def sentMail(order_id, my_cart):
    order = get_object_or_404(Order, id = order_id )
    subject = f'Order nr. {order.id}'
    first_message = f'Dear {order.first_name},\n\n You have successfully placed an order with MASMAD. Your order ID is {order.id}. Here is what you ordered: '
    message = first_message + str(my_cart.cart_info())
    mail_sent = send_mail(subject,
    message,
    'ngoniechizororo@gmail.com',
    [order.email])
    print("Mail sent")
    return mail_sent
        
        

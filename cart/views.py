from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from products.models import Product
from .cart import Cart 
from django.views.decorators.http import require_POST
from rest_framework.views import APIView
from rest_framework.response import Response as MyResponse
from rest_framework import permissions, status

#This thing was a menace, Still needs testing
#I thought I had seen enough DRF to build something meaningfull
#Until I wrote these serializerless APIViews :-)


class CartView(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        cart = Cart(request)
        data = request.session['cart']
        return MyResponse(cart.cart_info(), status=status.HTTP_200_OK)

    def post(self, request):
        product_id = request.data['product_id']
        cart = Cart(request)
        print(request.data)
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity =int(request.data['quantity']), override_quantity = request.data['override_quantity'])
        data = request.session['cart']
        return MyResponse(cart.cart_info(), status=status.HTTP_200_OK)
        
class CartRemoveView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        cart = Cart(request)
        product_id = request.data['product_id']
        product = get_object_or_404(Product, id = product_id)
        cart.remove(product)
        return MyResponse(cart.cart_info(), status=status.HTTP_200_OK)







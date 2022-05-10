from django.contrib import admin

from .models import Order, OrderItems, Cart, CartItem




admin.site.register(Order)
admin.site.register(OrderItems)
admin.site.register(Cart)
admin.site.register(CartItem)


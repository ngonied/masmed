from django.db import models
from users.models import CustomUser
from products.models import Product



class Order(models.Model):
    order = models.IntegerField(null = False, unique = True)
    #customer = models.ForeignKey(CustomUser, related_name = "order", on_delete =models.CASCADE)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    created = models.DateField( auto_now_add=True)
    price = models.DecimalField( max_digits=6, decimal_places=2, default = 0)
    updated = models.DateTimeField(auto_now=True)
    courier = models.ForeignKey(CustomUser, blank = True, null = True, on_delete = models.CASCADE)
    delivered = models.BooleanField(default=False)
    pescription = models.FileField(upload_to="files/pescriptions", max_length=100)
    payed = models.BooleanField(default=False)
    date = models.DateField(auto_now=True, auto_now_add=False)


    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return f'Order {self.id}'
    
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order,related_name='items',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='order_items',on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return str(self.id)
    
    def get_cost(self):
        return self.price * self.quantity
    




# class OrderItems(models.Model):
#     item = models.ForeignKey(Product, related_name ="orderItems", on_delete=models.CASCADE)
#     order = models.ForeignKey(Order, related_name ="orderItems", on_delete = models.CASCADE )
#     quantity = models.IntegerField(default=1)

#     class Meta:
#         verbose_name_plural = 'Order Items'

#     def __str__(self):
#         return self.item
    


# class Cart(models.Model):
#     customer = models.ForeignKey(CustomUser, on_delete =models.CASCADE)
#     cart_id = models.CharField(max_length = 200)
#     pescription = models.FileField( upload_to='files/pescriptions', max_length=100, null = True)
#     paid = models.BooleanField(default=False)
#     date = models.DateField(auto_now_add=True)
#     pay_on_delivery = models.BooleanField(default= False)

#     def get_total_price(self):
#         return self.items_set.all()


# class CartItem(models.Model):
#     cart = models.ForeignKey(Cart, related_name = 'items', on_delete = models.CASCADE)
#     product = models.ForeignKey(Product, on_delete = models.CASCADE)
#     quantity = models.PositiveIntegerField(default = 1)

#     def __str__(self):
#         return '{} {}'.format(self.product.name, self.quantity)
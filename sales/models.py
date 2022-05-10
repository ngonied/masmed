from django.db import models
from users.models import CustomUser
from products.models import Product



class Order(models.Model):
    order = models.IntegerField(null = False, unique = True)
    customer = models.ForeignKey(CustomUser, related_name = "order", on_delete =models.CASCADE)
    price = models.DecimalField( max_digits=6, decimal_places=2, default = 0)
    delivered = models.BooleanField(default=False)
    pescription = models.FileField(upload_to="files/pescriptions", max_length=100)
    payment = models.BooleanField(default=False)
    date = models.DateField(auto_now=True, auto_now_add=False)


    def __str__(self):
        return self.customer + self.order
    


    




class OrderItems(models.Model):
    item = models.ForeignKey(Product, related_name ="orderItems", on_delete=models.CASCADE)
    order = models.ForeignKey(Order, related_name ="orderItems", on_delete = models.CASCADE )
    quantity = models.IntegerField(default=1)

    class Meta:
        verbose_name_plural = 'Order Items'

    def __str__(self):
        return self.item
    


class Cart(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete =models.CASCADE)
    cart_id = models.CharField(max_length = 200)
    pescription = models.FileField( upload_to='files/pescriptions', max_length=100, null = True)
    paid = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)
    pay_on_delivery = models.BooleanField(default= False)

    def get_total_price(self):
        total_price = 0
        for item in self.items_set.all():
            total_price += item.product.price

    def __iter__(self):
        products = self.items.set_all()
        for product in products:
            total_price += product.product.price * product.quantity
            yield total_price


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name = 'items', on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default = 1)

    def __str__(self):
        return '{} {}'.format(self.product.name, self.quantity)
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
    

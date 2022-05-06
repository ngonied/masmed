from django.db import models
from users.models import CustomUser

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantityInProduct = models.CharField(max_length=50)
    quantityInStock = models.IntegerField(default = 0)
    image = models.ImageField()
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete = models.CASCADE)

    


class Category(models.Model):
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 100)







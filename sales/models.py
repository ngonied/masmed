from django.db import models
from users.models import CustomUser


class Order(models.Model):
    order = models.IntegerField(null = False, unique = True)
    customer = models.ForeignKey(CustomUser, on_delete =models.CASCADE)
    price = models.DecimalField( max_digits=6, decimal_places=2, default = 0)
    delivered = models.BooleanField(default=False)
    pescription = models.FileField(upload_to="files/pescriptions", max_length=100)
    payment = models.BooleanField(default=False)

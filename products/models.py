from django.db import models
from users.models import CustomUser
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save




class Product(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(blank = True, null = True)
    description = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantityInProduct = models.CharField(max_length=50)
    quantityInStock = models.IntegerField(default = 0)
    image = models.ImageField(upload_to="files/products/images")
    seller = models.ForeignKey(CustomUser, related_name = "products", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", related_name ="products", on_delete = models.CASCADE)
    overTheCounter = models.BooleanField(default =False)
    created = models.DateField( auto_now_add=True)
    updated = models.DateField( auto_now=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    
    


def product_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug  = slugify(instance.name)
        exists= Product.objects.filter(slug=instance.slug).exists() #check if slug exists

        if exists:
            
            
            num = Product.objects.filter(name=instance.name).count() #count number of objects with similar name
        
            instance.slug = "%s-%s"%(instance.slug, num + 1)
        
        instance.slug = instance.slug

    
pre_save.connect(product_pre_save, sender = Product, weak=False)



class Category(models.Model):
    
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 100)
    slug = models.SlugField(null=True, blank = True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    


def category_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        
        instance.slug  = slugify(instance.name)
        exists= Category.objects.filter(slug=instance.slug).exists() #check if slug exists

        if exists:
            
            
            num = Category.objects.filter(name=instance.name).count() #count number of objects with similar name
        
            instance.slug = "%s-%s"%(instance.slug, num + 1)
        
        instance.slug = instance.slug

    
pre_save.connect(category_pre_save, sender = Category, weak=False)



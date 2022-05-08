from django.contrib import admin
from .models import *



# admin.site.register(Product)
# admin.site.register(Category)



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    
    list_display = ['name', 'description', 'manufacturer', 'price', 'quantityInProduct','quantityInStock', 'image', 'seller', 'category','overTheCounter', 'created']
    list_filter = ['available', 'created', 'updated']
    


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

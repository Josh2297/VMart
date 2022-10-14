from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=('product_name','product_category','creator')
    list_filter=('product_category','availability')
    search_fields=('product_category__icontains','product_name__icontains')
admin.site.register(Product,ProductAdmin)
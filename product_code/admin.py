from django.contrib import admin
from .models import Product


class AdminProduct(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'product_code']
    list_filter = ['product_name', 'product_code']
    search_fields = ['product_name', 'product_code']

admin.site.register(Product, AdminProduct)

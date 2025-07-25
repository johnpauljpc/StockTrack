from django.contrib import admin
from .models import Category, Product

# Register your models here.
admin.site.register(Category)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'unit_price','available_quantity', 'total_price']
admin.site.register(Product, ProductAdmin)

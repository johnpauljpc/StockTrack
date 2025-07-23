from django.contrib import admin
from .models import Category, Product, Customer, Supplier

# Register your models here.
admin.site.register(Category)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'unit_price', 'total_price']
admin.site.register(Product, ProductAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'email', 'phone_number','age']

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Supplier, CustomerAdmin)
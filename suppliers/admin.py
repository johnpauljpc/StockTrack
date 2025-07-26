from django.contrib import admin
from .models import Supplier

# Register your models here.
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'email', 'phone_number','age']

admin.site.register(Supplier, SupplierAdmin)
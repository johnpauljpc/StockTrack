from django.contrib import admin
from .models import Customer

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'email', 'phone_number','age']

admin.site.register(Customer, CustomerAdmin)

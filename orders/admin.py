from django.contrib import admin
from .models import IncomingOrder, OutgoingOrder

# Register your models here.
admin.site.register(IncomingOrder)
admin.site.register(OutgoingOrder)

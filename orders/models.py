from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from products.models import Product, Supplier, Customer

# Create your models here.


class IncomingOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True) #add related words
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)
    quantity_supply = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=20, decimal_places=2, editable=False)
    supply_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.total_price = self.product.unit_price * self.quantity_supply
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.product} - {self.supplier}"
    

class OutgoingOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    quantity_order = models.PositiveIntegerField(default=1)
    total_price_before_discount = models.DecimalField(max_digits=20, decimal_places=2, editable=False)
    discount = models.DecimalField(validators=[MinValueValidator(0), MaxValueValidator(100)], max_digits=2, decimal_places=2, default=0)
    total_price_after_discount = models.DecimalField(max_digits=20, decimal_places=2, editable=False)
    order_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        subtotal = self.product.unit_price * self.quantity_supply
        self.total_price_before_discount = subtotal
        self.total_price_after_discount = subtotal - subtotal*(self.discount / 100) if self.discount >=0 and self.discount <= 100 else subtotal
        return super().save(*args, **kwargs)

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from products.models import Product
from customers.models import Customer
from suppliers.models import Supplier

# Create your models here.


class IncomingOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE) #add related words
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    quantity_supply = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=20, decimal_places=2, editable=False)
    supply_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        is_new = self._state.adding

        if not is_new:
            original = IncomingOrder.objects.get(pk=self.pk)
            quantity_diff = self.quantity_supply - original.quantity_supply
        else:
            quantity_diff = self.quantity_supply

        self.product.available_quantity += quantity_diff

        if self.product.available_quantity < 0:
            raise ValueError("Cannot reduce stock below zero.")

        self.product.save()

        self.total_price = self.quantity_supply * self.product.unit_price

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.product.available_quantity -= self.quantity_supply

        if self.product.available_quantity < 0:
            raise ValueError("Deleting this would cause negative stock.")

        self.product.save()
        super().delete(*args, **kwargs)
        
    
    def __str__(self):
        return f"{self.product} - {self.supplier}"
    

class OutgoingOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
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

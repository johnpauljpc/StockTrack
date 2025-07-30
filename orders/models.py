from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from products.models import Product
from customers.models import Customer
from suppliers.models import Supplier

# Create your models here.


class IncomingOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # add related words
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    quantity_supply = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=20, decimal_places=2, editable=False)
    supply_date = models.DateTimeField(auto_now_add=True)

    def clean(self):
        is_new = self._state.adding

        if not is_new:
            original = IncomingOrder.objects.get(pk=self.pk)
            quantity_diff = self.quantity_supply - original.quantity_supply
        else:
            quantity_diff = self.quantity_supply

        new_quantity = self.product.available_quantity + quantity_diff

        if new_quantity < 0:
            raise ValidationError({
                "quantity_supply": f"Your reduction exceeds the available quantity of '{self.product.name}'."
            })
        
  

    def save(self, *args, **kwargs):
        is_new = self._state.adding

        if not is_new:
            original = IncomingOrder.objects.get(pk=self.pk)
            quantity_diff = self.quantity_supply - original.quantity_supply
        else:
            quantity_diff = self.quantity_supply

        self.product.available_quantity += quantity_diff


        self.product.save()

        self.total_price = self.quantity_supply * self.product.unit_price

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.product.available_quantity -= self.quantity_supply

        if self.product.available_quantity < 0:
            self.product.available_quantity = 0
            # raise ValueError("Deleting this would cause negative stock.")

        self.product.save()
        super().delete(*args, **kwargs)

    """def save(self, *args, **kwargs):
        self.total_price = self.quantity_supply * self.product.unit_price
        current_product = Product.objects.get(pk = self.product.pk)
        super().save(*args, **kwargs) #saves incoming order
        current_ordered_product_qs = IncomingOrder.objects.filter(product = current_product)
        

        # Get total quantity of a given product
        total_availability = sum([product.quantity_supply for product in current_ordered_product_qs if product.quantity_supply > 0])
        self.product.available_quantity = total_availability
        self.product.save()

    def delete(self, *args, **kwargs):
        current_product = Product.objects.get(pk = self.product.pk)
        super().delete(*args, **kwargs)
        current_ordered_product_qs = IncomingOrder.objects.filter(product = current_product)

        # Get total quantity of a given product
        total_availability = sum([product.quantity_supply for product in current_ordered_product_qs if product.quantity_supply > 0])
        self.product.available_quantity = total_availability
        self.product.save()

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              

        
    """

    def __str__(self):
        return f"{self.quantity_supply} {self.product} - {self.supplier}"


class OutgoingOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity_order = models.PositiveIntegerField(default=1)
    total_price_before_discount = models.DecimalField(
        max_digits=20, decimal_places=2, editable=False
    )
    discount = models.DecimalField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        max_digits=5,
        decimal_places=2,
        default=0,
    )
    total_price_after_discount = models.DecimalField(
        max_digits=20, decimal_places=2, editable=False
    )
    order_date = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.quantity_order > self.product.available_quantity:
            raise ValidationError(
                {
                    "quantity_order": f"Requested quantity exceeds stock. Only {self.product.available_quantity} available for '{self.product.name}'."
                }
            )

    def save(self, *args, **kwargs):
        subtotal = self.product.unit_price * self.quantity_order
        self.total_price_before_discount = subtotal
        self.total_price_after_discount = (
            subtotal - subtotal * (self.discount / 100)
            if self.discount >= 0 and self.discount <= 100
            else subtotal
        )

        if self.pk: #checks if order already exits
            original_order = OutgoingOrder.objects.get(pk=self.pk)
            if original_order.product == self.product: #if the product is the same
                diff_qty = self.quantity_order - original_order.quantity_order
                self.product.available_quantity -= diff_qty
                self.product.save()
            
            # products are not the same
            else:
                original_order.product.available_quantity += original_order.quantity_order
                original_order.product.save()
                self.product.available_quantity -=  self.quantity_order
                self.product.save()


        else: # Entirely new, newly created
            self.product.available_quantity -= self.quantity_order
            self.product.save()
        

        return super().save(*args, **kwargs)
    

    def delete(self, *args, **kwargs):
        #Restores the stock
        self.product.available_quantity += self.quantity_order
        self.product()
        return super().delete(*args, **kwargs)

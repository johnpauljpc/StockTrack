from django.db import models



# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length = 100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    available_quantity = models.PositiveIntegerField(default=0, editable=False)
    unit_price = models.DecimalField(decimal_places=2, default=0.00, max_digits=10)
    total_price = models.DecimalField(decimal_places=2, max_digits=20,editable=False)
    date_created = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        self.total_price = self.unit_price * self.available_quantity
        return super().save(*args, **kwargs)

    @property
    def availability(self):
        if self.available_quantity:
            return "Yes, Available"
        return "No, Not Available"
    
    @property 
    def total_amount_of_all_products(self):
        products = Product.objects.all()
        total_amount = sum([product.total_price for product in products if product.total_price > 0 ])
        return total_amount


    def __str__(self):
        return self.name


   

    

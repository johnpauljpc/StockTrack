from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length = 100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    available_quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(decimal_places=2, default=0.00, max_digits=10)
    total_price = models.DecimalField(decimal_places=2, max_digits=20,editable=False)
    date_created = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        self.total_price = self.unit_price * self.available_quantity
        return super().save(*args, **kwargs)


    def __str__(self):
        return self.name
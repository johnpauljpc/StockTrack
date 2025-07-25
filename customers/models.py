from django.db import models
from datetime import date
from dateutil.relativedelta import relativedelta

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    date_created = models.DateTimeField(auto_now_add=True)

        #age derieved from date of birth
    @property 
    def age(self):
        current_date = date.today()
        return relativedelta(current_date, self.date_of_birth).years


    def __str__(self):
        return self.first_name

    

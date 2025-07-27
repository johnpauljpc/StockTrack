from django import forms
from .models import IncomingOrder, Product, Supplier



class IncomingOrderForm(forms.ModelForm):
    product = forms.ModelChoiceField(
        queryset=Product.objects.all(),
        empty_label="Select Product",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    supplier = forms.ModelChoiceField(
        queryset=Supplier.objects.all(),
        empty_label="Select Supplier",
        widget=forms.Select(attrs={'class': 'form-control'})
    )


    class Meta:
        model = IncomingOrder
        fields = ['product','supplier', 'quantity_supply']
        widgets ={
            'quantity_supply':forms.NumberInput(attrs={'class':'form-control'})

        }

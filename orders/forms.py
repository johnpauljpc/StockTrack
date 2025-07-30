from django import forms
from .models import IncomingOrder, Product, Supplier, OutgoingOrder,Customer



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


class OutgoingOrderForm(forms.ModelForm):
    product = forms.ModelChoiceField(
        queryset=Product.objects.all(),
        empty_label="Select Product",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    customer = forms.ModelChoiceField(
        queryset=Customer.objects.all(),
        empty_label="Select Customer",
        widget=forms.Select(attrs={'class': 'form-control'})
    )


    class Meta:
        model = OutgoingOrder
        fields = ['product','customer', 'quantity_order', 'discount']
        widgets ={
            'quantity_order':forms.NumberInput(attrs={'class':'form-control'}),
            'discount':forms.NumberInput(attrs={'class':'form-control'})

        }
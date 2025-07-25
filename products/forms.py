from django import forms
from .models import Category, Product


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'e.g. drinks'}),
           'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Just a short description.'})
        }

class ProductForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="Select Category",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    class Meta:
        model = Product
        fields = ['name','unit_price', 'category']

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            # 'available_quantity':forms.NumberInput(attrs={'class':'form-control'}),
            'unit_price':forms.NumberInput(attrs={'class':'form-control'}),
            
        }
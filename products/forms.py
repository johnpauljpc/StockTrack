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
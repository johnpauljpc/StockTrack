from django import forms
from .models import Customer



class CustomerForm(forms.ModelForm):
    # category = forms.ModelChoiceField(
    #     queryset=Category.objects.all(),
    #     empty_label="Select Category",
    #     widget=forms.Select(attrs={'class': 'form-control'})
    # )
    class Meta:
        model = Customer
        fields = ['first_name','last_name', 'date_of_birth', 'email', 'phone_number', 'address']

        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'date_of_birth':forms.DateInput(attrs={'class':'form-control', "type":"date"}),
            'email':forms.EmailInput(attrs={'class':'form-control', "type":"email"}),
            'phone_number':forms.TextInput(attrs={'class':'form-control', "type":"tel"}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            
        }
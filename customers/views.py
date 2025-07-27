from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView,DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from .models import Customer
from .forms import CustomerForm


# Create your views here.

class CustomerListView(ListView):
    model = Customer
    context_object_name = "Customers"
    template_name = 'Customers/Customer_list.html'

   
class CustomerCreateView(SuccessMessageMixin, CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = "Customers/create_Customer.html"
    success_url = reverse_lazy("list_Customers")
    def get_success_message(self, cleaned_data):
        return f"New Customer - ({self.object.first_name}) created successfully."
    

    

class UpdateCustomerView(SuccessMessageMixin,UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = "Customers/update_Customer.html"
    success_url = reverse_lazy("list_Customers")
    success_messages = "Customer updated successfully!"

class DeleteCustomerView(DeleteView):
    model = Customer
    context_object_name = 'Customer'
    template_name = "Customers/delete_Customer.html"
    success_url = reverse_lazy("list_Customers")
    # success_message = "deleted"

    def form_valid(self, form):
        Customer = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        messages.success(self.request, f"Customer: {Customer.name} deleted!")
        return redirect(success_url)
       

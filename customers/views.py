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
    context_object_name = "customers"
    template_name = 'Customers/Customer_list.html'

   
class CustomerCreateView(SuccessMessageMixin, CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = "Customers/create_Customer.html"
    success_url = reverse_lazy("list_customers")
    def get_success_message(self, cleaned_data):
        return f"New Customer - ({self.object.first_name}) created successfully."
    

    

class UpdateCustomerView(SuccessMessageMixin,UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = "customers/update_customer.html"
    success_url = reverse_lazy("list_customers")
    success_messages = "Customer updated successfully!"

class DeleteCustomerView(DeleteView):
    model = Customer
    context_object_name = 'customer'
    template_name = "customers/delete_customer.html"
    success_url = reverse_lazy("list_customers")
    # success_message = "deleted"

    def form_valid(self, form):
        customer = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        messages.success(self.request, f"Customer: {customer.first_name} deleted!")
        return redirect(success_url)
       

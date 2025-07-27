from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView,DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from .models import Supplier
from .forms import SupplierForm


# Create your views here.

class SupplierListView(ListView):
    model = Supplier
    context_object_name = "suppliers"
    template_name = 'suppliers/supplier_list.html'

   
class SupplierCreateView(SuccessMessageMixin, CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = "suppliers/create_supplier.html"
    success_url = reverse_lazy("list_suppliers")
    def get_success_message(self, cleaned_data):
        return f"New supplier - ({self.object.first_name}) created successfully."
    

    

class UpdateSupplierView(SuccessMessageMixin,UpdateView):
    model = Supplier
    form_class = SupplierForm
    template_name = "Suppliers/update_Supplier.html"
    success_url = reverse_lazy("list_suppliers")
    success_messages = "Supplier updated successfully!"

class DeleteSupplierView(DeleteView):
    model = Supplier
    context_object_name = 'supplier'
    template_name = "Suppliers/delete_Supplier.html"
    success_url = reverse_lazy("list_suppliers")
    # success_message = "deleted"

    def form_valid(self, form):
        supplier = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        messages.success(self.request, f"Supplier: {supplier.name} deleted!")
        return redirect(success_url)
       

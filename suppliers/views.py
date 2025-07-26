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
    
# class DetailProducView(DetailView):
#     model = Product
#     context_object_name = "product"
#     template_name = 'products/product_detail.html'

    

# class UpdateProductView(SuccessMessageMixin,UpdateView):
#     model = Product
#     form_class = ProductForm
#     template_name = "products/update_product.html"
#     success_url = reverse_lazy("product_list")
#     success_messages = "Product updated successfully!"

# class DeleteProductView(DeleteView):
#     model = Product
#     context_object_name = 'product'
#     template_name = "products/delete_product.html"
#     success_url = reverse_lazy("product_list")
#     # success_message = "deleted"

#     def form_valid(self, form):
#         cat = self.get_object()
#         success_url = self.get_success_url()
#         self.object.delete()
#         messages.success(self.request, f"Cat: {cat.name} deleted!")
#         return redirect(success_url)
       

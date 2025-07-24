from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from .models import Product, Category
from .forms import CategoryForm


# Create your views here.

class ListCategoryView(ListView):
    model = Category
    context_object_name = "categories"
    template_name = 'category/category_list.html'

class CreateCategoryView(SuccessMessageMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "category/create_category.html"
    success_url = reverse_lazy("category_list")
    def get_success_message(self, cleaned_data):
        return f"New category - ({self.object.name}) created successfully."
    

class UpdateCategoryView(SuccessMessageMixin,UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = "category/update_category.html"
    success_url = reverse_lazy("category_list")
    success_messages = "Category updated successfully!"

class DeleteCategoryView(DeleteView):
    model = Category
    context_object_name = 'category'
    template_name = "category/delete_category.html"
    success_url = reverse_lazy("category_list")
    # success_message = "deleted"

    def form_valid(self, form):
        cat = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        messages.success(self.request, f"Cat: {cat.name} deleted!")
        return redirect(success_url)
       


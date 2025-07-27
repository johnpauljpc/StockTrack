from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView,DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from .models import IncomingOrder
from .forms import IncomingOrderForm


# Create your views here.

class IncomingOrderListView(ListView):
    model = IncomingOrder
    context_object_name = "incoming_orders"
    template_name = 'orders/incoming/list_orders.html'

   
class IncomingOrderCreateView(SuccessMessageMixin, CreateView):
    model = IncomingOrder
    form_class = IncomingOrderForm
    template_name = "orders/incoming/create_order.html"
    success_url = reverse_lazy("list_incoming_orders")
    def get_success_message(self, cleaned_data):
        return f"New Incoming order - ({self.object}) made successfully."
    

    

class IncomingOrderUpdateView(SuccessMessageMixin,UpdateView):
    model = IncomingOrder
    form_class = IncomingOrderForm
    template_name = "orders/incoming/update_order.html"
    success_url = reverse_lazy("list_incoming_orders")
    success_messages = "Incoming order updated successfully!"

class IncomingOrderDeleteView(DeleteView):
    model = IncomingOrder
    context_object_name = 'incoming_order'
    template_name = "orders/incoming/delete_order.html"
    success_url = reverse_lazy("list_incoming_orders")
    # success_message = "deleted"

    def form_valid(self, form):
        incoming_order = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        messages.success(self.request, f"order: {incoming_order} deleted!")
        return redirect(success_url)
       

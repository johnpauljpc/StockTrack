from django.urls import path
from .views import SupplierListView,SupplierCreateView


urlpatterns = [
    path("", SupplierListView.as_view(), name="list_suppliers"),
    path("create/", view=SupplierCreateView.as_view(), name="create_supplier"), 
]
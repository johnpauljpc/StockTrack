from django.urls import path
from .views import SupplierListView,SupplierCreateView, UpdateSupplierView, DeleteSupplierView


urlpatterns = [
    path("", SupplierListView.as_view(), name="list_suppliers"),
    path("create/", view=SupplierCreateView.as_view(), name="create_supplier"),
    path("update/<pk>/", view=UpdateSupplierView.as_view(), name="update_supplier"),
    path("delete/<pk>/", view=DeleteSupplierView.as_view(), name="delete_supplier"), 
]
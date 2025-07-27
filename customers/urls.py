from django.urls import path
from .views import CustomerListView,CustomerCreateView, UpdateCustomerView, DeleteCustomerView


urlpatterns = [
    path("", CustomerListView.as_view(), name="list_customers"),
    path("create/", view=CustomerCreateView.as_view(), name="create_customer"),
    path("update/<pk>/", view=UpdateCustomerView.as_view(), name="update_customer"),
    path("delete/<pk>/", view=DeleteCustomerView.as_view(), name="delete_customer"), 
]
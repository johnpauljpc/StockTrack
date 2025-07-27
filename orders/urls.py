from django.urls import path
from .views import IncomingOrderListView, IncomingOrderCreateView, IncomingOrderUpdateView, IncomingOrderDeleteView

urlpatterns = [
    path('incoming/', view=IncomingOrderListView.as_view(), name="list_incoming_orders"),
    path('incoming/create/', view=IncomingOrderCreateView.as_view(), name="create_incoming_order"),
    path("incoming/update/<pk>/", view=IncomingOrderUpdateView.as_view(), name="update_incoming_order"),
    path('incoming/delete/<pk>/', view=IncomingOrderDeleteView.as_view(), name="delete_incoming_order"),
]
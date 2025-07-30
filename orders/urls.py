from django.urls import path
from .views import (IncomingOrderListView, IncomingOrderCreateView, IncomingOrderUpdateView, IncomingOrderDeleteView,
                    OutgoingOrderListView, OutgoingOrderCreateView, OutgoingOrderUpdateView, OutgoingOrderDeleteView)

urlpatterns = [
    path('incoming/', view=IncomingOrderListView.as_view(), name="list_incoming_orders"),
    path('incoming/create/', view=IncomingOrderCreateView.as_view(), name="create_incoming_order"),
    path("incoming/update/<pk>/", view=IncomingOrderUpdateView.as_view(), name="update_incoming_order"),
    path('incoming/delete/<pk>/', view=IncomingOrderDeleteView.as_view(), name="delete_incoming_order"),

    # Outgoing orders
    path('outgoing/', view=OutgoingOrderListView.as_view(), name="list_outgoing_orders"),
    path('outgoing/create/', view=OutgoingOrderCreateView.as_view(), name="create_outgoing_order"),
    path("outgoing/update/<pk>/", view=OutgoingOrderUpdateView.as_view(), name="update_outgoing_order"),
    path('outgoing/delete/<pk>/', view=OutgoingOrderDeleteView.as_view(), name="delete_outgoing_order"),
]
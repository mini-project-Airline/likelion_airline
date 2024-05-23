from django.urls import path
from .views import TicketListView, PurchaseTicketView, RefundTicketView

urlpatterns = [
    path('tickets', TicketListView.as_view(), name='get_tickets'),
    path('purchase/<int:ticket>', PurchaseTicketView.as_view(), name='purchase_ticket'),
    path('tickets/<int:ticketId>/refund', RefundTicketView.as_view(), name='refund_ticket'),
]

from django.urls import path
from .views import health, list_orders

urlpatterns = [
    path('health/', health, name='Health'),
    path('orders/', list_orders, name='OrdersList'),
]

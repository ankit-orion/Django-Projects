# pizza_order/urls.py
from django.urls import path
from .views import order_pizza

urlpatterns = [
    path('', order_pizza, name='order_pizza'),
]

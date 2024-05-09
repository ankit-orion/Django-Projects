# bookings/urls.py
from django.urls import path
from .views import book_travel, booking_success

urlpatterns = [
    path('', book_travel, name='book_travel'),
    path('success/', booking_success, name='booking_success'),
]

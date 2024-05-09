# reservation/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.reserve_book, name='reserve_book'),
    path('success/', views.reservation_success, name='reservation_success'),
]

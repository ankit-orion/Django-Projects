# marks/urls.py
from django.urls import path
from .views import marksheet

urlpatterns = [
    path('', marksheet, name='marksheet'),
]

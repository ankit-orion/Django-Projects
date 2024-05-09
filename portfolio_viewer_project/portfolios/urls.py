# portfolios/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio_list, name='portfolio_list'),
    path('portfolio/<int:portfolio_id>/', views.portfolio_detail, name='portfolio_detail'),
]

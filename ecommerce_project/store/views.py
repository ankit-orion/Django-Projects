# store/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {'title': 'Home'})

def about(request):
    return render(request, 'about.html', {'title': 'About Us'})

def products(request):
    products_data = [
        {'name': 'Product 1', 'price': 10.99},
        {'name': 'Product 2', 'price': 19.99},
        {'name': 'Product 3', 'price': 29.99},
    ]
    return render(request, 'products.html', {'title': 'Products', 'products': products_data})

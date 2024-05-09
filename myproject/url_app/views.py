# url_app/views.py
from django.http import JsonResponse

def home(request):
    return JsonResponse({'message': 'Welcome to the home page!'})

def about(request):
    return JsonResponse({'message': 'This is the about page.'})

def contact(request):
    return JsonResponse({'message': 'Contact us at contact@example.com'})

def user_profile(request, username):
    return JsonResponse({'message': f'User profile for {username}'})

def product_detail(request, product_id):
    return JsonResponse({'message': f'Details for product with ID {product_id}'})

def category_items(request, category):
    return JsonResponse({'message': f'Items in the category: {category}'})

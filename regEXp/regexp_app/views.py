# regexp_app/views.py
from django.http import JsonResponse

def get_user_by_id(request, user_id):
    data = {'user_id': user_id, 'message': 'This is a sample user information by ID'}
    return JsonResponse(data)

def get_user_by_name(request, user_name):
    data = {'user_name': user_name, 'message': 'This is a sample user information by name'}
    return JsonResponse(data)

# myapp/views.py
from django.shortcuts import render
from django.http import HttpResponse

def set_cookie(request):
    response = HttpResponse("Cookie set!")
    response.set_cookie('username', 'john_doe', max_age=3600)  # Set cookie with a username for 1 hour
    return response

def get_cookie(request):
    username = request.COOKIES.get('username')
    if username:
        return HttpResponse(f"Hello, {username}! Welcome back.")
    else:
        return HttpResponse("No cookie found!")

def delete_cookie(request):
    response = HttpResponse("Cookie deleted!")
    response.delete_cookie('username')
    return response

def set_session(request):
    request.session['user_id'] = 123  # Set session variable 'user_id' with value 123
    return HttpResponse("Session set!")

def get_session(request):
    user_id = request.session.get('user_id')
    if user_id:
        return HttpResponse(f"User ID: {user_id}")
    else:
        return HttpResponse("No session found!")

def delete_session(request):
    if 'user_id' in request.session:
        del request.session['user_id']  # Delete session variable 'user_id'
        return HttpResponse("Session deleted!")
    else:
        return HttpResponse("No session found!")

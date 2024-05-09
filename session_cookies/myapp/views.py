from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def set_cookies(request):
    response =HttpResponse("Cookie set")
    response.set_cookie('username','rahul', max_age=3600)
    #set cookies for 1hour
    return response
def get_cookies(request):
    username=request.COOKIES.get('username')
    if username:
        return HttpResponse(f"hello, {username}! welcome Back")
    else:
        return HttpResponse("No cookies found")
def delete_cookies(request):
    response=HttpResponse("cookies deleted")
    response.delete_cookie('username')
    return response
def set_session(request):
    request.session['user_id']=878# set session with userid with value 878
    return HttpResponse("Session Set")
def get_session(request):
    user_id=request.session.get('user_id')
    if user_id:
        return HttpResponse(f                           
0bn
jjjjj'USER Id:{user_id}')
    else:
        return HttpResponse("No session found")
def delete_session(request):                                                                                                                                                                                                 
    if 'user_id' in request.session:
        del request.session['user_id']
        return HttpResponse("session is deleted")
    else:
        return HttpResponse("No seesion found")
    
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import User

def signup(request):
    account_created = False
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create(username=username, email=email, password=password)
        user.save()
        account_created = True    
    return render(request, 'signup.html', {'account_created': account_created})

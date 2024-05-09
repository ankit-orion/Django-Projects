from django.shortcuts import render

# Create your views here.
# myapp/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

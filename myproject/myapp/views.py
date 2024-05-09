from django.shortcuts import render

# Create your views here.
# File: myapp/views.py

from django.shortcuts import render
from .models import MyModel

def index(request):
    data = MyModel.objects.all()
    return render(request, 'index.html', {'data': data})

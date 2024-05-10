from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegistrationForm(UserCreationForm):
    phone = forms.CharField(max_length=15)
    role = forms.CharField(max_length=100)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'role', 'password1', 'password2']

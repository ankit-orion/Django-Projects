# reservation/forms.py
from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['user', 'book', 'return_date']
        widgets = {'return_date': forms.DateInput(attrs={'type': 'date'})}

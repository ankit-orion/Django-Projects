# marks/forms.py
from django import forms
from .models import Mark

class MarkForm(forms.ModelForm):
    class Meta:
        model = Mark
        fields = ['student_name', 'subject_name', 'marks']

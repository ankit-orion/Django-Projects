# feedback_app/forms.py
from django import forms

class FeedbackForm(forms.Form):
    RATING_CHOICES = [(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]
    SATISFACTION_CHOICES = [('yes', 'Yes'), ('no', 'No')]
    DEPARTMENT_CHOICES = [('sales', 'Sales'), ('support', 'Support'), ('finance', 'Finance'), ('hr', 'Human Resources')]
    TOPIC_CHOICES = [('website', 'Website'), ('product', 'Product'), ('customer_service', 'Customer Service'), ('pricing', 'Pricing')]
    
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email')
    rating = forms.ChoiceField(label='Rating', choices=RATING_CHOICES, widget=forms.RadioSelect)
    comments = forms.CharField(label='Comments', widget=forms.Textarea(attrs={'rows': 6}))
    department = forms.ChoiceField(label='Department', choices=DEPARTMENT_CHOICES, widget=forms.Select)
    topics = forms.MultipleChoiceField(label='Feedback Topics', choices=TOPIC_CHOICES, widget=forms.CheckboxSelectMultiple)
    satisfied = forms.ChoiceField(label='Are you satisfied with our services?', choices=SATISFACTION_CHOICES, widget=forms.RadioSelect)
    additional_info = forms.CharField(label='Additional Information', required=False, widget=forms.Textarea(attrs={'rows': 4}))

from django.shortcuts import render

# Create your views here.
# feedback_app/views.py
from django.shortcuts import render
from .forms import FeedbackForm

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Process the form data
            # For demonstration purposes, just printing the data here
            print(form.cleaned_data)
            return render(request, 'thank_you.html')
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})

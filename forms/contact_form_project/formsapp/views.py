from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import ContactForm

def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data (send email, save to database, etc.)
            # For demonstration purposes, we'll just print the form data
            print(form.cleaned_data)
            return render(request, 'thank_you.html')
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form})

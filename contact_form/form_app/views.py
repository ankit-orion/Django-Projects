from django.shortcuts import render

# Create your views here.
from .forms import ContactForm 
def contact_form(request):
    
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # proceess the form data (send email;)
            # print 
            print(form.cleaned_data)
            return render(request, 'thankyou.html')
    else:
        form=ContactForm()

    
    return render(request, 'contact_form.html',{'form':form})
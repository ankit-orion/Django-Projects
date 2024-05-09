# marks/views.py
from django.shortcuts import render, redirect
from .forms import MarkForm
from .models import Mark

def marksheet(request):
    if request.method == 'POST':
        form = MarkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('marksheet')
    else:
        form = MarkForm()
    marks = Mark.objects.all()
    return render(request, 'marksheet.html', {'form': form, 'marks': marks})

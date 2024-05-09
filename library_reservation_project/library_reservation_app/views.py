from django.shortcuts import render

# Create your views here.
# reservation/views.py
from django.shortcuts import render, redirect
from .forms import ReservationForm

def reserve_book(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservation_success')
    else:
        form = ReservationForm()
    return render(request, 'reserve_book.html', {'form': form})

def reservation_success(request):
    return render(request, 'success.html')

# bookings/views.py
from django.shortcuts import render, redirect
from .forms import BookingForm

def book_travel(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'booking_success.html')
    else:
        form = BookingForm()
    return render(request, 'booking_form.html', {'form': form})

def booking_success(request):
    return render(request, 'booking_success.html')

from django.shortcuts import render

# Create your views here.
# pizza_order/views.py
from django.shortcuts import render
from .forms import PizzaOrderForm

def order_pizza(request):
    if request.method == 'POST':
        form = PizzaOrderForm(request.POST)
        if form.is_valid():
            # Process the form data (save to database, etc.)
            return render(request, 'order_success.html')
    else:
        form = PizzaOrderForm()
    return render(request, 'order_pizza.html', {'form': form})

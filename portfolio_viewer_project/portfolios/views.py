from django.shortcuts import render

# Create your views here.
# portfolios/views.py
from django.shortcuts import render

def portfolio_list(request):
    portfolios = [
        {'id': 1, 'name': 'Portfolio 1', 'description': 'This is the description of Portfolio 1.', 'owner': 'John Doe'},
        {'id': 2, 'name': 'Portfolio 2', 'description': 'This is the description of Portfolio 2.', 'owner': 'Alice Smith'},
        {'id': 3, 'name': 'Portfolio 3', 'description': 'This is the description of Portfolio 3.', 'owner': 'Bob Johnson'},
    ]
    return render(request, 'portfolio_list.html', {'portfolios': portfolios})

def portfolio_detail(request, portfolio_id):
    portfolio = {'id': portfolio_id, 'name': f'Portfolio {portfolio_id}', 'description': f'This is the description of Portfolio {portfolio_id}.', 'owner': f'Owner {portfolio_id}'}
    return render(request, 'portfolio_detail.html', {'portfolio': portfolio})

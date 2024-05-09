# library/views.py
from django.shortcuts import render

def home(request):
    # Sample data for demonstration
    book1 = {'title': 'Book 1', 'author': 'Author 1', 'genre': 'Fiction'}
    book2 = {'title': 'Book 2', 'author': 'Author 2', 'genre': 'Non-fiction'}

    context = {
        'book1': book1,
        'book2': book2
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def books(request):
    # Return a list of books
    books = [
        {'title': 'Book 1', 'author': 'Author 1', 'genre': 'Fiction'},
        {'title': 'Book 2', 'author': 'Author 2', 'genre': 'Non-fiction'},
        {'title': 'Book 3', 'author': 'Author 3', 'genre': 'Science Fiction'},
    ]
    return render(request, 'books.html', {'books': books})

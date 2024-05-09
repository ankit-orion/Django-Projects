from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def student_list(request):
    students = [
        {"name": "John", "age": 20, "grade": "A"},
        {"name": "Jane", "age": 21, "grade": "B"},
        {"name": "Alice", "age": 19, "grade": "A+"},
    ]
    return render(request, 'student_list.html', {'students': students})

from django.shortcuts import render

# Create your views here.
from .models import Blogpost
def blogpost(request, id):
    # post = Blogpost.objects.filter(post_id = id).first()
    post = Blogpost.objects.filter(post_id = id)[0]
    print(post)
    return render(request, 'blogpost.html',{'post':post})
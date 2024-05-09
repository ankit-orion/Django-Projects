from django.shortcuts import render, get_object_or_404
from .models import Blog, Post

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog_list.html', {'blogs': blogs})

def post_list(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    posts = blog.posts.all()
    return render(request, 'post_list.html', {'blog': blog, 'posts': posts})

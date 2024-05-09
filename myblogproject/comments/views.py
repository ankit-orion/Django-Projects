
# Create your views here.
from django.shortcuts import render, redirect
from .models import Comment
from .forms  import CommentForm

def add_comment(request, post_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_id = post_id
            comment.save()
            return redirect('post_detail', post_id=post_id)
    else:
        form = CommentForm()
    return render(request, 'add_comment.html', {'form': form})

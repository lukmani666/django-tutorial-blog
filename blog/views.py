from django.shortcuts import render
from .models import Post
from .forms import PostForm

def index(request):
    if request.method == 'POST':
        form = PostForm()
        if form.is_valid():
            post = Post.objects.create()
            post.save()
            form.save()
    else:
        form = PostForm()
    return render(request, 'blog/index.html', {'form': form})
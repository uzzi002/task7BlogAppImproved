from django.shortcuts import render
from .models import Post

def post_list(request):
    """
    Display a list of published blog posts.
    Fetches all blog posts from the database and renders
    them in the 'post_list.html' template.
    """
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

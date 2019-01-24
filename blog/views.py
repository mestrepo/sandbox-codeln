from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):
    """a view to display the list of posts."""
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})

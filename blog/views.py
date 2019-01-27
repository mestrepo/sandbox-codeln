from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView

from .models import Post


class PostListView(ListView):
    """a class-based view to display the list of posts."""
    queryset = Post.published.all()  # object list
    context_object_name = 'posts'  # context variable for query results, defaults to object_list
    paginate_by = 1  # number of posts per page
    template_name = 'blog/post/list.html'  # rendering template


def post_list(request):
    """a view to display the list of posts."""
    object_list = Post.published.all()
    paginator = Paginator(object_list, 1)  # number of posts per page
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)  # deliver first page if page is not an integer
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)  # deliver last page if page is out of range

    return render(request, 'blog/post/list.html', {'page': page, 'posts': posts})


def post_detail(request, year, month, day, post):
    """a view to display details of a single post."""
    post = get_object_or_404(
        Post,
        slug=post,
        status='published',
        publish__year=year,
        publish__month=month,
        publish__day=day
    )
    return render(request, 'blog/post/detail.html', {'post': post})

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView

from .models import Job


class JobListView(ListView):
    """a class-based view to display the list of posts."""
    queryset = Job.objects.all()  # object list
    context_object_name = 'jobs'  # context variable for query results, defaults to object_list
    # paginate_by = 1  # number of posts per page
    template_name = 'marketplace/developer/jobs/list.html'  # rendering template


def job_detail(request, year, month, day, post):
    """a view to display details of a single post."""
    # post = get_object_or_404(
    #     Post,
    #     slug=post,
    #     status='published',
    #     publish__year=year,
    #     publish__month=month,
    #     publish__day=day
    # )
    # return render(request, 'blog/post/detail.html', {'post': post})
    pass

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView

from .models import Job


def dev_home(request):
    """a view to show developer home on marketplace."""
    return render(request, 'marketplace/developer/home.html')


class JobListView(ListView):
    """a class-based view to display the list of posts."""
    queryset = Job.objects.all()  # object list
    context_object_name = 'jobs'  # context variable for query results, defaults to object_list
    # paginate_by = 1  # number of posts per page
    template_name = 'marketplace/developer/jobs/list.html'  # rendering template


def job_detail(request, year, month, day, job):
    """a view to display details of a single post."""
    job = get_object_or_404(
        Job,
        slug=job,
        position_filled=False,
        created__year=year,
        created__month=month,
        created__day=day
    )
    return render(request, 'marketplace/developer/jobs/detail.html', {'job': job})

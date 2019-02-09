from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView

from .models import Job, Recruiter, Developer, JobApplication
from .forms import JobForm


def dev_home(request):
    """a view to show developer's home on marketplace."""
    return render(request, 'marketplace/developer/home.html')


def job_list(request):
    """a view to display the list of jobs."""
    jobs = Job.objects.all()

    developer = Developer.objects.get(auth_user__username=request.user)

    applied_jobs = developer.applied_jobs.all()

    return render(request, 'marketplace/developer/jobs/list.html',
                  {'jobs': jobs, 'applied_jobs': [j_a.job for j_a in applied_jobs]})


def job_detail(request, year, month, day, job):
    """a view to display details of a single job."""
    job = get_object_or_404(
        Job,
        slug=job,
        position_filled=False,
        created__year=year,
        created__month=month,
        created__day=day
    )

    applied = True if request.GET['applied'] == 'True' else False

    return render(request, 'marketplace/developer/jobs/detail.html',
                  {'job': job, 'job_applied_status': applied})


def recruiter_home(request):
    """a view to show recruiter's home on marketplace."""
    return render(request, 'marketplace/recruiter/home.html')


def post_job(request):
    """a view to post a job."""
    recruiter = Recruiter.objects.get(auth_user__username=request.user)

    if request.method == 'POST':
        job_form = JobForm(data=request.POST)
        if job_form.is_valid():
            new_job = job_form.save(commit=False)
            new_job.posted_by = recruiter
            new_job.save()
            job_form = JobForm()
    else:
        job_form = JobForm()

    return render(request, 'marketplace/recruiter/jobs/create.html', {'job_form': job_form})


def apply_for_job(request, job_id):
    """a view to apply for a job."""
    if request.method == 'POST':
        job = Job.objects.get(id=job_id)

        developer = Developer.objects.get(auth_user__username=request.user)

        developer.applied_jobs.get_or_create(job=job)

        return HttpResponseRedirect("/marketplace/dev/job_list/")
    else:
        return HttpResponseRedirect("/marketplace/dev/job_list/")

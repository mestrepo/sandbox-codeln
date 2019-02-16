from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Job, Recruiter, Developer, JobApplication, Person
from .forms import JobForm


def user_dashboard(request):
    """a view to show developer's home on marketplace."""
    user_is_recruiter = False

    user = Person.objects.get(auth_user__username=request.user)

    user_has_posted_jobs = False

    try:
        if isinstance(user.recruiter, Recruiter):
            user_is_recruiter = True
            user_has_posted_jobs = True if Job.objects.filter(posted_by=user.recruiter).first() else False
    except:
        pass

    if user_is_recruiter:
        return render(request, 'marketplace/recruiter/home.html', {'user_has_posted_jobs': user_has_posted_jobs})
    return render(request, 'marketplace/developer/home.html')


def job_list(request):
    """a view to display the list of jobs."""
    jobs = Job.objects.all()

    developer = Developer.objects.get(auth_user__username=request.user)

    applied_jobs = developer.applied_jobs.all()

    return render(request, 'marketplace/developer/jobs/list.html',
                  {'jobs': jobs, 'applied_jobs': [j_a.job for j_a in applied_jobs]})


def dev_job_detail(request, year, month, day, job):
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


def recruiter_job_detail(request, job_id, list_of_applicants, list_selected_devs):
    """a view to display job_details of a single job."""
    job = Job.objects.get(id=job_id)

    selected_candidates = []
    applicants = []

    if list_selected_devs != 'NONE':
        dev_ids = list_selected_devs.split(",")
        for _id in dev_ids:
            dev_id = int(_id)
            try:
                selected_candidates.append(Developer.objects.get(id=dev_id))
            except:
                pass
    else:
        pass

    if list_of_applicants != 'NONE':
        dev_ids = list_of_applicants.split(",")
        for _id in dev_ids:
            dev_id = int(_id)
            try:
                developer = Developer.objects.get(id=dev_id)
                if developer not in selected_candidates:
                    applicants.append(developer)
            except:
                pass
    else:
        pass

    return render(request, 'marketplace/recruiter/jobs/detail.html',
                  {'job': job, 'applicants': applicants, 'selected_candidates': selected_candidates})


def post_job(request):
    """a view to post a job."""
    recruiter = Recruiter.objects.get(auth_user__username=request.user)

    if request.method == 'POST':
        job_form = JobForm(data=request.POST)
        if job_form.is_valid():
            new_job = job_form.save(commit=False)
            new_job.posted_by = recruiter
            new_job.save()
            # job_form = JobForm()
            return HttpResponseRedirect("/marketplace/recruiter/manage_posted_jobs/")
    else:
        job_form = JobForm()
        return render(request, 'marketplace/recruiter/jobs/create.html', {'job_form': job_form})


def apply_for_job(request, job_id):
    """a view to apply for a job."""
    if request.method == 'POST':
        job = Job.objects.get(id=job_id)

        job_application, was_created = JobApplication.objects.get_or_create(job=job)

        job_application.applied_by.add(Developer.objects.get(auth_user__username=request.user))

        return HttpResponseRedirect("/marketplace/dev/job_list/")
    else:
        return HttpResponseRedirect("/marketplace/dev/job_list/")


def manage_posted_jobs(request):
    """a view to display the list of jobs."""
    jobs = Job.objects.filter(posted_by=Recruiter.objects.get(auth_user__username=request.user))

    job_details = []

    all_selected_candidates = None
    all_applicants = None

    for job in jobs:
        try:
            all_selected_candidates = JobApplication.objects.get(job=job).selected_devs.all()
            all_applicants = JobApplication.objects.get(job=job).applied_by.all()
        except:
            pass

        if all_selected_candidates:
            selected_candidates = [dev.id for dev in all_selected_candidates]
        else:
            selected_candidates = []

        if all_applicants:
            applied_by = [dev.id for dev in all_applicants]
        else:
            applied_by = []

        job_details.append((job, applied_by, selected_candidates))

    return render(request, 'marketplace/recruiter/jobs/list.html',
                  {'job_details': job_details})


def pick_candidate(request, job_id, dev_id):
    job = Job.objects.get(id=job_id)

    job_application, was_created = JobApplication.objects.get_or_create(job=job)

    job_application.selected_devs.add(Developer.objects.get(id=dev_id))

    return HttpResponseRedirect("/marketplace/recruiter/manage_posted_jobs/")


def get_recommended_developers():
    pass

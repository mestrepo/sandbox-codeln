from django import forms
from .models import Job


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ('posted_by', 'created', 'updated', 'position_filled',)

# posted_by = models.ForeignKey(Recruiter, related_name='posted_jobs', on_delete=models.CASCADE)
#     title = models.CharField(max_length=255)
#     # field to build beautiful, SEO-friendly URLs for job posts
#     # prevent multiple jobs from having the same slug for the same date
#     slug = models.SlugField(max_length=250, unique_for_date='created')
#     description = models.TextField()
#     job_role = models.CharField(max_length=30, choices=JOB_ROLE, default='full_stack_developer')
#     dev_experience = models.CharField(max_length=30, choices=DEV_EXPERIENCE, default='mid-level')
#     engagement_type = models.CharField(max_length=30, choices=ENGAGEMENT_TYPE, default='full_time')
#     tech_stack = models.CharField(max_length=500)
#     num_devs_wanted = models.IntegerField(default=1)
#     # monthly remuneration for fulltime, contract etc. budget project for freelance
#     remuneration_in_dollars = models.CharField(max_length=45, help_text='in dollars ($)')
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#     position_filled = models.BooleanField(default=False)

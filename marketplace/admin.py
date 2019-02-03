from django.contrib import admin
from .models import Recruiter, Developer, Job, JobStatistic

admin.site.register(Recruiter)
admin.site.register(Developer)
admin.site.register(Job)
admin.site.register(JobStatistic)

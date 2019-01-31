from django.contrib import admin

from .models import Recruiter, Developer, JobDetails, Job


admin.site.register(Recruiter)
admin.site.register(Developer)
admin.site.register(JobDetails)
admin.site.register(Job)
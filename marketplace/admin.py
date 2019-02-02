from django.contrib import admin

from .models import Recruiter, Developer, JobDetail, Job


admin.site.register(Recruiter)
admin.site.register(Developer)
admin.site.register(JobDetail)
admin.site.register(Job)
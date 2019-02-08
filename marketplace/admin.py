from django.contrib import admin
from .models import Recruiter, Developer, Job, JobApplication


class JobAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Recruiter)
admin.site.register(Developer)
admin.site.register(Job, JobAdmin)
admin.site.register(JobApplication)

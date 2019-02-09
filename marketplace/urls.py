from django.conf.urls import url
from django.urls import path
from django.views.generic import RedirectView

from . import views
app_name = 'marketplace'

urlpatterns = [
    path('dev/', views.dev_home, name='dev_home'),
    path('dev/job_list/', views.job_list, name='job_list'),
    path('dev/job_detail/<int:year>/<int:month>/<int:day>/<str:job>/', views.job_detail, name='job_detail'),
    path('dev/apply_for_job/<int:job_id>/', views.apply_for_job, name='apply_for_job'),

    path('recruiter/', views.recruiter_home, name='recruiter_home'),
    path('recruiter/post_job/', views.post_job, name='post_job'),
]

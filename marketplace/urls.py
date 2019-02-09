from django.urls import path

from . import views

app_name = 'marketplace'

urlpatterns = [
    path('', views.user_dashboard, name='user_dashboard'),
    path('dev/', views.user_dashboard, name='user_dashboard'),
    path('recruiter/', views.user_dashboard, name='user_dashboard'),

    path('dev/job_list/', views.job_list, name='job_list'),
    path('dev/job_detail/<int:year>/<int:month>/<int:day>/<str:job>/', views.job_detail, name='job_detail'),
    path('dev/apply_for_job/<int:job_id>/', views.apply_for_job, name='apply_for_job'),

    path('recruiter/post_job/', views.post_job, name='post_job'),
]

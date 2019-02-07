from django.urls import path

from . import views

app_name = 'marketplace'

urlpatterns = [
    path('', views.dev_home, name='dev_home'),
    path('dev/job_list/', views.JobListView.as_view(), name='job_list'),
    path('dev/job_detail/<int:year>/<int:month>/<int:day>/<str:job>/', views.job_detail, name='job_detail'),
]
from django.urls import path

from . import views

app_name = 'marketplace'

urlpatterns = [
    path('', views.JobListView.as_view(), name='job_list'),
    path('<int:year>/<int:month>/<int:day>/<str:post>/', views.job_detail, name='job_detail'),
]
from django.urls import path,include

from .views import dashboard,viewapplication,dashboard_job

urlpatterns=[
    path('',dashboard,name="dashboard"),
    path('application/<int:application_id>/',viewapplication,name='viewapplication'),
    path('job/<int:job_id>/',dashboard_job,name='dashboard_job')

]
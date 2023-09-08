from django.urls import path,include
from .api import search_job

from .views import addjob,job_detail,apply_for_job,search,edit_job

urlpatterns=[
    path('search/',search, name='search'),
    path('api/search',search_job,name='search_job'),
    path('add/',addjob,name="add_job"),
    path('<int:job_id>/',job_detail,name='job_detail'),
    path('<int:job_id>/edit_job/',edit_job,name='edit_job'),
    path('<int:job_id>/apply_for_job',apply_for_job,name="apply_for_job")
]
from django.urls import path
from job.views import (
    job,
    job_create,
    job_delete,
    jobs,
)

urlpatterns = [
    path('all/', jobs, name='jobs'),
    path('<int:id>/', job, name='artist-job'),
    path('create/', job_create, name='job-create'),
    path('delete/<int:job_id>/', job_delete, name='job-delete'),
]

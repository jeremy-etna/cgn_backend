from django.urls import path
from job.views import (
    job,
    job_creation,
    jobs,
)

urlpatterns = [
    path('jobs/', jobs, name='jobs'),
    path('job/<id>', job, name='artist-job'),
    path('creation/', job_creation, name='job-creation'),
]

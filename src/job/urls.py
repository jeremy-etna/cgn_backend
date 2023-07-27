from django.urls import path
from job.views import (
    # job,
    # job_create,
    # job_delete,
    # jobs,
    # R E S T
    JobListView,
    JobView,
    JobCreateView,
)

urlpatterns = [
    # path('all/', jobs, name='jobs'),
    # path('<int:id>/', job, name='artist-job'),
    # path('create/', job_create, name='job-create'),
    # path('delete/<int:job_id>/', job_delete, name='job-delete'),
    # R E S T
    path('test/', JobListView.as_view(), name='job-test'),
    path('test/<int:id>/', JobView.as_view(), name='job-test-id'),
    path('test/create/', JobCreateView.as_view(), name='job-test-create'),
]

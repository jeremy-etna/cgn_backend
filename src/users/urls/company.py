from django.urls import path
from users.views.company import profile, profile_edit, job_create, job, artists, artist, jobs, job_delete

urlpatterns = [
    path('profile/', profile, name='company-profile'),
    path('profile/edit/', profile_edit, name='company-profile-edit'),
    path('artists/', artists, name='company-artists'),
    path('artist/<id>', artist, name='company-artist'),
    path('jobs/', jobs, name='company-jobs'),
    path('jobs/create/', job_create, name='company-job-create'),
    path('jobs/delete/<id>', job_delete, name='company-job-delete'),
    path('job/<id>', job, name='company-job'),
]

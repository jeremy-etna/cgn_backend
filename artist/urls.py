from django.urls import path

from .views import profile, profile_edit, jobs, companies, company, job

urlpatterns = [
    path('profile/', profile, name='artist-profile'),
    path('profile/edit/', profile_edit, name='artist-profile-edit'),
    path('jobs', jobs, name='artist-jobs'),
    path('job/<id>', job, name='artist-job'),
    path('companies', companies, name='artist-companies'),
    path('company/<id>', company, name='artist-company'),
]

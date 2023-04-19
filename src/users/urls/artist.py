from django.urls import path
from users.views.artist import profile, profile_edit, artists, companies, company

urlpatterns = [
    path('profile/', profile, name='artist-profile'),
    path('profile/edit/', profile_edit, name='artist-profile-edit'),
    path('artists/', artists, name='artists-gallery'),
    path('companies/', companies, name='companies-gallery'),
    path('company/<id>/', company, name='artist-company'),
]

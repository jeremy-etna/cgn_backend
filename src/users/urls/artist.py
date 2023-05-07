from django.urls import path
from users.views.artist import profile, ProfileEditView, artists, companies, company

urlpatterns = [
    path('profile/', profile, name='artist-profile'),
    path('profile/edit/', ProfileEditView.as_view(), name='artist-profile-edit'),
    path('artists/', artists, name='artist-artists-gallery'),
    path('companies/', companies, name='artist-companies-gallery'),
    path('company/<id>/', company, name='artist-company'),
]

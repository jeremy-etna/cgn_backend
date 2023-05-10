from django.urls import path
from users.views.company import profile, ProfileEditView, artist, artists, company, companies

urlpatterns = [
    path('profile/', profile, name='company-profile'),
    path('profile/edit/', ProfileEditView.as_view(), name='company-profile-edit'),
    path('artists/', artists, name='company-artists-gallery'),
    path('companies/', companies, name='company-companies-gallery'),
    path('artist/<id>/', artist, name='company-artist'),
    path('company/<id>/', company, name='company-company'),
]
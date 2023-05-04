from django.urls import path
from users.views.company import profile, ProfileEditView, artists, companies

urlpatterns = [
    path('profile/', profile, name='company-profile'),
    path('profile/edit/', ProfileEditView.as_view(), name='company-profile-edit'),
    path('artists/', artists, name='artists-gallery'),
    path('companies/', companies, name='companies-gallery'),
]
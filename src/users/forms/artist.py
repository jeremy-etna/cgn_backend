from django.forms import ModelForm
from users.models.artist import Artist
from cgnetwork.models import (
    Coordinate,
    Contract,
    SocialMedia,
    Sector,
    Competence,
    Software,
)


class ArtistIdentityForm(ModelForm):
    class Meta:
        model = Artist
        exclude = ['user']


class ArtistCoordinateForm(ModelForm):
    class Meta:
        model = Coordinate
        exclude = ['user']


class ArtistContractForm(ModelForm):
    class Meta:
        model = Contract
        exclude = ['user']


class ArtistSocialMediaForm(ModelForm):
    class Meta:
        model = SocialMedia
        exclude = ['user']


class ArtistSectorForm(ModelForm):
    class Meta:
        model = Sector
        exclude = ['user']


class ArtistCompetenceForm(ModelForm):
    class Meta:
        model = Competence
        exclude = ['user']


class ArtistSoftwareForm(ModelForm):
    class Meta:
        model = Software
        exclude = ['user']

from django.forms import ModelForm


from users.models.artist import (
    ArtistIdentity,
    ArtistCoordinate,
    ArtistAdministrative,
    ArtistMobility,
    ArtistContract,
    ArtistSocialMedia,
    ArtistSector,
    ArtistCompetence,
    ArtistSoftware,
)


class ArtistIdentityForm(ModelForm):
    class Meta:
        model = ArtistIdentity
        exclude = ['user']


class ArtistCoordinateForm(ModelForm):
    class Meta:
        model = ArtistCoordinate
        exclude = ['user']


class ArtistAdministrativeForm(ModelForm):
    class Meta:
        model = ArtistAdministrative
        exclude = ['user']


class ArtistMobilityForm(ModelForm):
    class Meta:
        model = ArtistMobility
        exclude = ['user']


class ArtistContractForm(ModelForm):
    class Meta:
        model = ArtistContract
        exclude = ['user']


class ArtistSocialMediaForm(ModelForm):
    class Meta:
        model = ArtistSocialMedia
        exclude = ['user']


class ArtistSectorForm(ModelForm):
    class Meta:
        model = ArtistSector
        exclude = ['user']


class ArtistCompetenceForm(ModelForm):
    class Meta:
        model = ArtistCompetence
        exclude = ['user']


class ArtistSoftwareForm(ModelForm):
    class Meta:
        model = ArtistSoftware
        exclude = ['user']

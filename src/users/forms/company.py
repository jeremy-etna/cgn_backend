from django.forms import ModelForm

from users.models.company import (
    CompanyIdentity,
    CompanyCoordinate,
    CompanyMobility,
    CompanySocialMedia,
    CompanySector,
    CompanyCompetence,
    CompanySoftware,
)


class CompanyIdentityForm(ModelForm):
    class Meta:
        model = CompanyIdentity
        exclude = ['user']


class CompanyCoordinateForm(ModelForm):
    class Meta:
        model = CompanyCoordinate
        exclude = ['user']


class CompanyMobilityForm(ModelForm):
    class Meta:
        model = CompanyMobility
        exclude = ['user']


class CompanySocialMediaForm(ModelForm):
    class Meta:
        model = CompanySocialMedia
        exclude = ['user']


class CompanySectorForm(ModelForm):
    class Meta:
        model = CompanySector
        exclude = ['user']


class CompanyCompetenceForm(ModelForm):
    class Meta:
        model = CompanyCompetence
        exclude = ['user']


class CompanySoftwareForm(ModelForm):
    class Meta:
        model = CompanySoftware
        exclude = ['user']

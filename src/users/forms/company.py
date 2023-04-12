from django.forms import ModelForm
from users.models.company import Company
from job.models import Job

from cgnetwork.models import (
    Coordinate,
    SocialMedia,
    Sector,
    Competence,
    Software,
)


class CompanyIdentityForm(ModelForm):
    class Meta:
        model = Company
        exclude = ['user']


class CompanyCoordinateForm(ModelForm):
    class Meta:
        model = Coordinate
        exclude = ['user']


class CompanySocialMediaForm(ModelForm):
    class Meta:
        model = SocialMedia
        exclude = ['user']


class CompanySectorForm(ModelForm):
    class Meta:
        model = Sector
        exclude = ['user']


class CompanyCompetenceForm(ModelForm):
    class Meta:
        model = Competence
        exclude = ['user']


class CompanySoftwareForm(ModelForm):
    class Meta:
        model = Software
        exclude = ['user']


class JobForm(ModelForm):
    class Meta:
        model = Job
        exclude = ['user']


class JobCompetenceForm(ModelForm):
    class Meta:
        model = Competence
        exclude = ['user']


class JobSoftwareForm(ModelForm):
    class Meta:
        model = Software
        exclude = ['user']



from django.forms import ModelForm
from job.models import Job

from users.models.company import (
    Company,
    CompanyCompetence,
    CompanySoftware,
)
from cgnetwork.models import (
    Coordinate,
    Mobility,
    SocialMedia,
    Sector,
)


class CompanyIdentityForm(ModelForm):
    class Meta:
        model = Company
        exclude = ['user']


class CompanyCoordinateForm(ModelForm):
    class Meta:
        model = Coordinate
        exclude = ['user']


class CompanyMobilityForm(ModelForm):
    class Meta:
        model = Mobility
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
        model = CompanyCompetence
        exclude = ['user']


class CompanySoftwareForm(ModelForm):
    class Meta:
        model = CompanySoftware
        exclude = ['user']


# class JobForm(ModelForm):
#     class Meta:
#         model = Job
#         exclude = ['user']
#
#
# class JobCompetenceForm(ModelForm):
#     class Meta:
#         model = Competence
#         exclude = ['user']
#
#
# class JobSoftwareForm(ModelForm):
#     class Meta:
#         model = Software
#         exclude = ['user']



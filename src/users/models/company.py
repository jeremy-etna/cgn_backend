from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator
from users.validators import validate_file_size
from cgnetwork.constants import (
    COMPETENCES,
    SOFTWARES,
    CompanySize,
)


class Company(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar = models.ImageField(
        upload_to='logos',
        default='logos/company_default.png',
        validators=[
            validate_file_size,
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])
        ])

    company_name = models.CharField(max_length=100)
    description = models.TextField()
    company_size = models.CharField(max_length=30, choices=CompanySize.choices)

    def __str__(self):
        return self.company_name


class CompanyCompetence(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    for competence in COMPETENCES:
        vars()[competence] = models.BooleanField(default=False)


class CompanySoftware(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    for software in SOFTWARES:
        vars()[software] = models.BooleanField(default=False)

from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator
from users.validators import validate_file_size

from cgnetwork.constants.models import (
    COMPETENCES,
    MOBILITIES,
    CONTRACTS,
    WEBSITES,
    SECTORS,
    SOFTWARES,
    CompanySize
)


class CompanyIdentity(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar = models.ImageField(
        upload_to="logos",
        default="logos/company_default.png",
        validators=[
            validate_file_size,
            FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png"]),
        ],
    )

    company_name = models.CharField(max_length=100)
    description = models.TextField()
    company_size = models.CharField(max_length=30, choices=CompanySize.choices)

    def __str__(self):
        return self.company_name


class CompanyCoordinate(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    country = models.CharField(max_length=60, blank=True)
    state = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=255, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)
    street_name = models.CharField(max_length=100, blank=True)
    street_number = models.CharField(max_length=10, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)


class CompanyContract(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    for contract in CONTRACTS:
        vars()[contract] = models.BooleanField(default=False)


class CompanyMobility(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    for mobility in MOBILITIES:
        vars()[mobility] = models.BooleanField(default=False)


class CompanySocialMedia(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    for website in WEBSITES:
        vars()[website] = models.URLField(max_length=255, blank=True)


class CompanySector(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    for sector in SECTORS:
        vars()[sector] = models.BooleanField(default=False)


class CompanyCompetence(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    for competence in COMPETENCES:
        vars()[competence] = models.BooleanField(default=False)


class CompanySoftware(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    for software in SOFTWARES:
        vars()[software] = models.BooleanField(default=False)

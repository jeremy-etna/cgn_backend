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
    SkillLevel,
)


class ArtistIdentity(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar = models.ImageField(
        upload_to='avatars',
        default='avatars/artist_default.png',
        validators=[
            validate_file_size,
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])
        ])
    title = models.CharField(max_length=50, blank=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)


class ArtistCoordinate(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    country = models.CharField(max_length=60, blank=True)
    state = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=255, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)
    street_name = models.CharField(max_length=100, blank=True)
    street_number = models.CharField(max_length=10, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)


class ArtistAdministrative(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    spectacle_number = models.CharField(max_length=10, blank=True)
    siret_number = models.CharField(max_length=14, blank=True)
    price = models.CharField(max_length=5, blank=True)


class ArtistContract(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    for contract in CONTRACTS:
        vars()[contract] = models.BooleanField(default=False)


class ArtistMobility(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    for mobility in MOBILITIES:
        vars()[mobility] = models.BooleanField(default=False)


class ArtistSocialMedia(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    for website in WEBSITES:
        vars()[website] = models.URLField(max_length=255, blank=True)


class ArtistSector(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    for sector in SECTORS:
        vars()[sector] = models.BooleanField(default=False)


class ArtistCompetence(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    for competence in COMPETENCES:
        vars()[competence] = models.CharField(max_length=30, choices=SkillLevel.choices)


class ArtistSoftware(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    for software in SOFTWARES:
        vars()[software] = models.CharField(max_length=30, choices=SkillLevel.choices)
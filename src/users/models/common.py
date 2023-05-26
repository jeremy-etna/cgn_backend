from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db.models.signals import post_save
from django.utils import timezone
from django.db import models

from django.conf import settings

from cgnetwork.constants.models import (
    Role,
)

from users.models.artist import (
    ArtistIdentity,
    ArtistCoordinate,
    ArtistAdministrative,
    ArtistContract,
    ArtistMobility,
    ArtistSocialMedia,
    ArtistSector,
    ArtistCompetence,
    ArtistSoftware,
)

from users.models.company import (
    CompanyIdentity,
    CompanyCoordinate,
    CompanyMobility,
    CompanySocialMedia,
    CompanySector,
    CompanyCompetence,
    CompanySoftware,
)


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user


class CustomUser(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True, blank=False)
    register_date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    role = models.CharField(max_length=30, choices=Role.choices)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['role']
    objects = CustomUserManager()

    def has_module_perms(self, app_label):
        return self.is_staff

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def __str__(self):
        return self.email


def post_save_receiver(sender, instance, created, **kwargs):
    if created:
        if instance.role == 'artist':
            ArtistIdentity.objects.create(user=instance)
            ArtistCoordinate.objects.create(user=instance)
            ArtistAdministrative.objects.create(user=instance)
            ArtistContract.objects.create(user=instance)
            ArtistMobility.objects.create(user=instance)
            ArtistSocialMedia.objects.create(user=instance)
            ArtistSector.objects.create(user=instance)
            ArtistCompetence.objects.create(user=instance)
            ArtistSoftware.objects.create(user=instance)

        elif instance.role == 'company':
            CompanyIdentity.objects.create(user=instance)
            CompanyCoordinate.objects.create(user=instance)
            CompanyMobility.objects.create(user=instance)
            CompanySocialMedia.objects.create(user=instance)
            CompanySector.objects.create(user=instance)
            CompanyCompetence.objects.create(user=instance)
            CompanySoftware.objects.create(user=instance)


post_save.connect(post_save_receiver, sender=settings.AUTH_USER_MODEL)

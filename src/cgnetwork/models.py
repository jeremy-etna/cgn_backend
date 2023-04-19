from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db.models.signals import post_save
from django.utils import timezone
from django.db import models


from django.conf import settings
from users.models.artist import Artist
from users.models.company import (
    Company,
    CompanyCompetence,
    CompanySoftware,
)
from cgnetwork.constants import (
    COMPETENCES,
    MOBILITIES,
    CONTRACTS,
    WEBSITES,
    SECTORS,
    SOFTWARES,
    UserRole,
    SkillLevel,
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
    user_role = models.CharField(max_length=30, choices=UserRole.choices)
    views = models.IntegerField(default=0)
    friends = models.ManyToManyField('self', blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_role']
    objects = CustomUserManager()

    def __str__(self):
        return self.email


def post_save_receiver(sender, instance, created, **kwargs):
    if created:
        if instance.user_role == 'artist':
            Artist.objects.create(user=instance)
            Coordinate.objects.create(user=instance)
            Mobility.objects.create(user=instance)
            Contract.objects.create(user=instance)
            Administrative.objects.create(user=instance)
            SocialMedia.objects.create(user=instance)
            Sector.objects.create(user=instance)
            Competence.objects.create(user=instance)
            Software.objects.create(user=instance)

        elif instance.user_role == 'company':
            Company.objects.create(user=instance)
            Coordinate.objects.create(user=instance)
            Mobility.objects.create(user=instance)
            SocialMedia.objects.create(user=instance)
            Sector.objects.create(user=instance)
            CompanyCompetence.objects.create(user=instance)
            CompanySoftware.objects.create(user=instance)


post_save.connect(post_save_receiver, sender=settings.AUTH_USER_MODEL)


class Coordinate(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    country = models.CharField(max_length=60, blank=True)
    state = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=255, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)
    street_name = models.CharField(max_length=100)
    street_number = models.CharField(max_length=10)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True)


class Mobility(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    for mobility in MOBILITIES:
        vars()[mobility] = models.BooleanField(default=False)


class Administrative(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    spectacle_number = models.CharField(max_length=10, blank=True)
    siret_number = models.CharField(max_length=14, blank=True)
    price = models.CharField(max_length=5, blank=True)


class Contract(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    for contract in CONTRACTS:
        vars()[contract] = models.BooleanField(default=False)


class SocialMedia(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    website = models.URLField(max_length=255, blank=True)
    for website in WEBSITES:
        vars()[website] = models.URLField(max_length=255, blank=True)


class Sector(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    for sector in SECTORS:
        vars()[sector] = models.BooleanField(default=False)


class Competence(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    for competence in COMPETENCES:
        vars()[competence] = models.CharField(max_length=30, choices=SkillLevel.choices)


class Software(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    for software in SOFTWARES:
        vars()[software] = models.CharField(max_length=30, choices=SkillLevel.choices)

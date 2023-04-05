from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.db.models.signals import post_save
from CgNetwork import settings
from artist.models import Artist
from company.models import Company
from django.utils import timezone


USER_ROLES = (
    ('artist', 'artist'),
    ('company', 'company')
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

    user_role = models.CharField(max_length=30, choices=USER_ROLES)
    country = models.CharField(max_length=60, blank=True)
    state = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=255, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)
    street_name = models.CharField(max_length=100)
    street_number = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_type']
    objects = CustomUserManager()

    def __str__(self):
        return self.email


def post_save_receiver(sender, instance, created, **kwargs):
    if created:
        if instance.user_role == 'artist':
            Artist.objects.create(user=instance)

        elif instance.user_role == 'company':
            Company.objects.create(user=instance)


post_save.connect(post_save_receiver, sender=settings.AUTH_USER_MODEL)

from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator
from users.validators import validate_file_size


class Artist(models.Model):
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

    def __str__(self):
        name = self.first_name + "_" + self.last_name
        return name

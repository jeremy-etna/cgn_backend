from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.db import models

from users.validators import validate_file_size
import urllib.parse as urlparse


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    likes = models.IntegerField(default=0)

    tags = models.CharField(max_length=200, blank=True)

    image = models.ImageField(
        upload_to="posts_images",
        validators=[
            validate_file_size,
            FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png"]),
        ],
        blank=True,
        null=True,
    )

    video_url = models.URLField(max_length=200, blank=True, null=True)

    social_link = models.URLField(max_length=200, blank=True, null=True)

    def get_youtube_video_id(self):
        url_data = urlparse.urlparse(self.video_url)
        return urlparse.parse_qs(url_data.query).get('v', [None])[0]

    def __str__(self):
        return self.title

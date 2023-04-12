from django.db import models
from django.conf import settings
from django.utils import timezone
from users.models.company import Company


class Job(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    creation_date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=100)
    description = models.TextField()
    salary_min = models.CharField(max_length=5)
    salary_max = models.CharField(max_length=5)

    def __str__(self):
        return self.title
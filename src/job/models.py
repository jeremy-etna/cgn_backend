from django.db import models
from django.conf import settings
from django.utils import timezone


class Job(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    creation_date = models.DateTimeField(default=timezone.now)

    title = models.CharField(max_length=100)
    company_description = models.TextField(default='')
    job_responsibilities = models.TextField(default='')
    required_skills = models.TextField(default='')
    required_qualifications = models.TextField(default='')
    job_requirements = models.TextField(default='')
    employee_benefits = models.TextField(default='')
    salary_min = models.CharField(max_length=5)
    salary_max = models.CharField(max_length=5)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
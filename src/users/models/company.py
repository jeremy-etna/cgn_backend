from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator
from users.validators import validate_file_size


class CompanySize(models.TextChoices):
    SIZE_1_10 = '1 - 10', '1 - 10'
    SIZE_11_50 = '11 - 50', '11 - 50'
    SIZE_51_99 = '51 - 99', '51 - 99'


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
    website = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name

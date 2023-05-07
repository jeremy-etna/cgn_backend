# Generated by Django 4.1.1 on 2023-05-05 06:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Job",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "creation_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("title", models.CharField(max_length=100)),
                ("company_description", models.TextField(default="")),
                ("job_responsibilities", models.TextField(default="")),
                ("required_skills", models.TextField(default="")),
                ("required_qualifications", models.TextField(default="")),
                ("job_requirements", models.TextField(default="")),
                ("employee_benefits", models.TextField(default="")),
                ("salary_min", models.CharField(max_length=5)),
                ("salary_max", models.CharField(max_length=5)),
                ("views", models.IntegerField(default=0)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
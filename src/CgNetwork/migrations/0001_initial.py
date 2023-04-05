# Generated by Django 4.1.1 on 2022-12-12 11:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('register_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True)),
                ('user_role', models.CharField(choices=[('artist', 'artist'), ('company', 'company')], max_length=30)),
                ('country', models.CharField(blank=True, max_length=60)),
                ('state', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(blank=True, max_length=255)),
                ('zip_code', models.CharField(blank=True, max_length=10)),
                ('street_name', models.CharField(max_length=100)),
                ('street_number', models.CharField(max_length=10)),
                ('phone_number', models.CharField(blank=True, max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
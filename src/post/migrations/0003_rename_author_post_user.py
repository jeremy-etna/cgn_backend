# Generated by Django 4.1.1 on 2023-06-15 15:31

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("post", "0002_alter_post_image"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="author",
            new_name="user",
        ),
    ]

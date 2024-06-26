# Generated by Django 5.0.1 on 2024-06-04 10:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("photo_gallery", "0004_photopost_authorized_delete_photoauth"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="photopost",
            name="authorized",
        ),
        migrations.CreateModel(
            name="PhotoAuth",
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
                ("authorized", models.BooleanField(default=False)),
                (
                    "photo_post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="auths",
                        to="photo_gallery.photopost",
                    ),
                ),
            ],
        ),
    ]

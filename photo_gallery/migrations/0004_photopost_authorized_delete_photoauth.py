# Generated by Django 5.0.1 on 2024-06-04 09:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("photo_gallery", "0003_alter_photopost_description_alter_photopost_likes"),
    ]

    operations = [
        migrations.AddField(
            model_name="photopost",
            name="authorized",
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name="PhotoAuth",
        ),
    ]

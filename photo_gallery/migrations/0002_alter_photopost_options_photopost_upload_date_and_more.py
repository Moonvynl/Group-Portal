# Generated by Django 5.0.6 on 2024-06-04 09:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("photo_gallery", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="photopost",
            options={"ordering": ["upload_date"]},
        ),
        migrations.AddField(
            model_name="photopost",
            name="upload_date",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="photoauth",
            name="authorized",
            field=models.BooleanField(default=False),
        ),
    ]

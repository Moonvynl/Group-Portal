# Generated by Django 5.0.1 on 2024-06-06 12:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "photo_gallery",
            "0012_alter_photoauth_options_remove_photoauth_authorized_and_more",
        ),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="photoauth",
            options={"ordering": ["-status"]},
        ),
        migrations.AlterField(
            model_name="photoauth",
            name="status",
            field=models.CharField(
                choices=[
                    ("1", "Підтверджено"),
                    ("2", "Йде перевірка"),
                    ("3", "Відхилино"),
                ],
                default="0",
                max_length=31,
            ),
        ),
    ]

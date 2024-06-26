# Generated by Django 5.0.1 on 2024-06-03 15:48

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("calendar_events", "0007_alter_event_options_remove_event_scheduled_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="scheduled_date",
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="event",
            name="scheduled_time",
            field=models.TimeField(null=True),
        ),
    ]

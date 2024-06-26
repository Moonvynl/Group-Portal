# Generated by Django 5.0.4 on 2024-06-07 15:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(default='avatars/default/default.png', upload_to='project_imgs/'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='projects',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='portfolio', to='user.project'),
        ),
    ]

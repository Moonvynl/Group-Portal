# Generated by Django 5.0.4 on 2024-06-07 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_alter_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, default='avatars/default/default.png', null=True, upload_to='project_imgs/'),
        ),
    ]

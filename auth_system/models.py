from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ACCESS_CHOICES = [
        ('user', 'User'),
        ('moder', 'Moderator'),
        ('admin', 'Admin')
    ]

    description = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='user-avatars/',  blank=True, null=False, default='avatars/default/default.png')
    access = models.CharField(max_length=31, choices=ACCESS_CHOICES, default='user')

    def __str__(self):
        return self.username
    
    class Meta():
        verbose_name = 'User'



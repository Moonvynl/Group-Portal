from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

class CustomUser(AbstractUser):
    ACCESS_CHOICES = [
        ('user', 'User'),
        ('moder', 'Moderator'),
        ('admin', 'Admin')
    ]

    description = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='user-avatars/',  blank=True, null=False, default='avatars/default/default.png')
    access = models.CharField(max_length=31, choices=ACCESS_CHOICES, default='user')
    raiting = models.IntegerField(
        default=0, 
        validators=[MinValueValidator(0),
        MaxValueValidator(5)]
    )

    def __str__(self):
        return self.username
    
    class Meta():
        verbose_name = 'User'


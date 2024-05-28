from django.db import models
from auth_system.models import CustomUser

# Create your models here.

class Advert(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='adverts')

    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='adverts-images/', blank=True, null=True)

    def __str__(self) -> str:
        return f'advert {self.title} by {self.author.username}'
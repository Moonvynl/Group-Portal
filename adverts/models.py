from django.db import models
from auth_system.models import CustomUser

# Create your models here.

class Advert(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='adverts')

    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='adverts-images/', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def shorten_content(self):
        if len(self.content) > 100:
            return self.content[:100] + '...'
        return self.content

    def __str__(self) -> str:
        return f'advert {self.title} by {self.author.username}'
    
    class Meta:
        ordering = ['-created']
        verbose_name = 'Advert'
        verbose_name_plural = 'Adverts'
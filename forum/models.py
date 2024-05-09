from django.db import models
from auth_system.models import CustomUser

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=98)

    def __str__(self) -> str:
        return f"Category - {self.name}"
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Topic(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='topics')
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='topics')

    title = models.CharField(max_length=98)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Topic {self.title} from {self.category.name} category"
    
    class Meta:
        verbose_name = 'Topic'
        verbose_name_plural = 'Topics'


class Post(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='posts')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='posts')

    title = models.CharField(max_length=98)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"post by {self.author.username} to {self.topic.title}"
    
    class Meta:
        ordering = ['created_at']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
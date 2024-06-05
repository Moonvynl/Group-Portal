from django.db import models
from auth_system.models import CustomUser
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
# Create your models here.

class PhotoPost(models.Model):
    author = models.ForeignKey(
        CustomUser,
        on_delete = models.CASCADE,
        related_name='photo_posts'
    )
    title = models.CharField(max_length=23, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="photo-gallery/")
    likes = models.ManyToManyField(CustomUser, related_name="liked_photo_posts", blank=True)
    upload_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-upload_date']


class PhotoAuth(models.Model):
    STATUS_CHOICES = [
        ('1', 'Підтверджено'),
        ('0', 'Йде перевірка'),
        ('-1', 'Відхилино')
    ]
    
    status = models.CharField(
        max_length=31,
        choices=STATUS_CHOICES,
        default="0"
    )

    photo_post = models.ForeignKey(
        PhotoPost,
        on_delete = models.CASCADE,
        related_name='auths',
        unique=True
    )
    details = models.CharField(max_length=63, null=True, blank=True)
    upload_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['status', '-upload_date']



@receiver(pre_delete, sender=PhotoPost)
def image_model_delete(sender, instance, **kwargs):
    if instance.image.name:
        instance.image.delete(False)
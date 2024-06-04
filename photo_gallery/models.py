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
    title = models.CharField(max_length=23, null=True)
    description = models.TextField()
    image = models.ImageField(blank=True, upload_to="photo-gallery/", null=True)
    likes = models.ManyToManyField(CustomUser, related_name="liked_photo_posts")


@receiver(pre_delete, sender=PhotoPost)
def image_model_delete(sender, instance, **kwargs):
    if instance.image.name:
        instance.image.delete(False)
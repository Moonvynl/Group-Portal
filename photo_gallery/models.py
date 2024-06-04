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
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(blank=True, upload_to="photo-gallery/", null=True)
    likes = models.ManyToManyField(CustomUser, related_name="liked_photo_posts", null=True, blank=True)
    upload_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['upload_date']


class PhotoAuth(models.Model):
    authorized = models.BooleanField(default=False)
    photo_post = models.ForeignKey(
        PhotoPost,
        on_delete = models.CASCADE,
        related_name='auths'
    )


@receiver(pre_delete, sender=PhotoPost)
def image_model_delete(sender, instance, **kwargs):
    if instance.image.name:
        instance.image.delete(False)
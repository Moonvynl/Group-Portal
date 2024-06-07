from django import template
from photo_gallery.models import PhotoAuth

register = template.Library()


@register.filter
def to_check_photo_posts(value):
    return len(PhotoAuth.objects.filter(status='3').all())

<<<<<<< HEAD
from django.conf import settings
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
=======
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
>>>>>>> 712ffd0f8bb20fd94e9693589a1f68a41100b19e
    additional_field = models.CharField(max_length=100)

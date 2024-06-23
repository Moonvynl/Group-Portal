from django.db import models
from auth_system.models import CustomUser


class Project(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='project')

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    git_url = models.URLField(blank=True)


class Image(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='project_imgs/', default='avatars/default/default.png', blank=True, null=True)


class Portfolio(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    projects = models.ManyToManyField(Project, blank=True, related_name='portfolio')

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    bio = models.CharField(max_length=250)
    github_url = models.URLField(blank=True)
    tg = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    adress = models.CharField(max_length=250, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

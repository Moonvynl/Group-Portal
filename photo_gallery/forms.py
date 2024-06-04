from django import forms
from photo_gallery.models import PhotoPost, PhotoAuth
from datetime import datetime
from django.utils import timezone


class PhotoPostForm(forms.ModelForm):
    class Meta:
        model = PhotoPost

        fields = [
            'title',
            'description',
            'image'
        ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput()
        }

        labels = {
            'title': 'Назва',
            'description': 'Опис',
            'image': 'Зображення:',
        }

class PhotoAuthForm(forms.ModelForm):
    class Meta:
        model = PhotoAuth

        fields = [
            'photo_post'
        ]

        widgets = {
            'photo_post': forms.TextInput(attrs={'class': 'form-control'})
        }

        labels = {
            'photo_post': 'Пост'
        }
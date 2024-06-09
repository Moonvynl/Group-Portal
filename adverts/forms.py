from django import forms
from .models import Advert


class AdvertCreationForm(forms.ModelForm):
    class Meta:
        model = Advert
        
        fields = [
            'title',
            'content',
            'image'
        ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput()
        }


class AdvertUpdateForm(forms.ModelForm):
    class Meta:
        model = Advert
        
        fields = [
            'title',
            'content',
            'image'
        ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
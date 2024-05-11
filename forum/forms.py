from django import forms
from .models import Category, Topic, Post

class CategoryCreationForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'name'
        ]

        labels = {
            'name': 'Enter category name:'
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }


class TopicCreationForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = [
            'title'
        ]

        labels = {
            'title': 'Enter topic title:'
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'})
        }


class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'content'
        ]

        labels = {
            'content': ''
        }

        widgets = {
            'content': forms.TextInput(attrs={'class': 'form-control'})
        }


class CategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'name'
        ]

        labels = {
            'name': 'Enter new category name:'
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }


class TopicUpdateForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = [
            'title'
        ]

        labels = {
            'title': 'Enter new topic title:'
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'})
        }


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'content'
        ]

        labels = {
            'content': 'New text'
        }

        widgets = {
            'content': forms.TextInput(attrs={'class': 'form-control'})
        }
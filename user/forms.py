from .models import Portfolio
from django import forms

class PortfolioCreationForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ('first_name',
                'last_name',
                'occupation',
                'bio',
                'github_url',
                'tg',
                'email',
                'adress',
                'phone',)
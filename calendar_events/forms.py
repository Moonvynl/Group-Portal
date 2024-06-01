from django import forms
from calendar_events.models import Event
from datetime import datetime
from django.utils import timezone


class EventCreateForm(forms.ModelForm):
    class Meta:
        model = Event

        fields = [
            'name',
            'description',
            'scheduled_date',
            'scheduled_time',
            'meeting_url',
        ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'scheduled_date': forms.SelectDateWidget(
                years=range(
                    timezone.now().year,
                    timezone.now().year + 5
                )
            ),
            'scheduled_time': forms.TimeInput(),
            'meeting_url': forms.TextInput(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(EventCreateForm, self).__init__(*args, **kwargs)
        self.fields['scheduled_date'].initial = timezone.now().date()
        self.fields['scheduled_time'].initial = timezone.now().date()
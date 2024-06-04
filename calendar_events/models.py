from django.db import models
from auth_system.models import CustomUser
from django.utils import timezone

class Event(models.Model):
    creator = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="events"
    )

    name = models.CharField(max_length=63)
    description = models.TextField(blank=True, null=True)

    scheduled_date = models.DateField(default=timezone.now)
    scheduled_time = models.TimeField(null=True)
    date_created = models.DateTimeField(auto_now=True)

    meeting_url = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ["scheduled_date"]

    
    def time(self):
        return self.scheduled_time.strftime("%H:%M")

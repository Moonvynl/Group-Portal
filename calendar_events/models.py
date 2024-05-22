from django.db import models
from auth_system.models import CustomUser

class Event(models.Model):
    creator = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="events"
    )

    name = models.CharField(max_length=63)
    description = models.TextField(blank=True, null=True)

    event_date = models.DateField(null=True, blank=True)
    event_time = models.TimeField(null=True, blank=True)
    creation_date = models.DateTimeField(auto_now=True)

    meeting_url = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ["event_date"]

    def __str__(self):
        return self.name

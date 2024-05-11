from django.urls import path
from calendar_events.views import CalendarEventListView
from django.urls import reverse_lazy

urlpatterns = [
    path('calendar/', CalendarEventListView.as_view(), name='calendar'),
]

app_name = 'calendar_event'
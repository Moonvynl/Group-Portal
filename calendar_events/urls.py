from django.urls import path
from calendar_events.views import view_date_events
from django.urls import reverse_lazy

urlpatterns = [
    path('calendar/', view_date_events, name='calendar_events'),
    path('calendar/<int:year>/<int:month>/<int:day>', view_date_events, name='events'),
]

app_name = 'calendar_event'
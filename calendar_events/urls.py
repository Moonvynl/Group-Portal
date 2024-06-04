from django.urls import path
from calendar_events.views import view_date_events, EventCreateView, EventDeleteView, EventUpdateView, EventListView
from django.urls import reverse_lazy

urlpatterns = [
    path('calendar/', view_date_events, name='calendar_events'),
    path('calendar/<int:year>/<int:month>/<int:day>', view_date_events, name='calendar_date'),
    path('event_list/', EventListView.as_view(), name='event_list'),
    path('create_event/', EventCreateView.as_view(), name="create_event"),
    path('delete_event/<int:pk>', EventDeleteView.as_view(), name="delete_event"),
    path('update_event/<int:pk>', EventUpdateView.as_view(), name="update_event"),
]

app_name = 'calendar_event'
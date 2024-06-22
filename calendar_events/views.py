from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseBadRequest
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from calendar_events.models import Event
from django.utils import timezone
from django.template.defaulttags import register
from calendar_events.events_func import next_date, previous_date, selected_date_events, month_events
from calendar_events.forms import EventCreateForm
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from calendar_events.mixins import UserIsOwnerMixin
import calendar
import datetime


root = "calendar_events/"
months = [
    ("Січень", "січня"),
    ("Лютий", "лютого"),
    ("Березень", "березня"),
    ("Квітень", "квітня"),
    ("Травень", "травня"),
    ("Червень", "червня"),
    ("Липень", "липня"),
    ("Серпень", "серпня"),
    ("Вересень", "вересня"),
    ("Жовтень", "жовтня"),
    ("Листопад", "листопада"),
    ("Грудень", "грудня")
]


def view_date_events(request, day=None, month=None, year=None):
    if not day or not month or not year:
        date = timezone.now()
    else:
        try:
            date = datetime.datetime(year, month, day)
        except:
            return HttpResponseBadRequest("Date not found") 
    
    paginator = Paginator(selected_date_events(date), 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "calendar": calendar.Calendar().monthdays2calendar(date.year, date.month),
        "today": timezone.now(),
        "date": date,
        "selected_date_events": page_obj,
        "events_month": month_events(date),
        "month_name": months[date.month-1],
        "next": next_date(date),
        "previous": previous_date(date),
    }

    return render(
        template_name=root+"calendar_page.html",
        context=context,
        request=request
    )

class EventListView(ListView, LoginRequiredMixin):
    model = Event
    template_name = root + "event/event_list.html"
    context_object_name = 'events'
    paginate_by = 7


class EventCreateView(CreateView, LoginRequiredMixin):
    model = Event
    template_name = root + "event/create_form.html"
    form_class = EventCreateForm
    success_url = reverse_lazy("calendar_event:calendar_events")

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class EventDeleteView(DeleteView, LoginRequiredMixin, UserIsOwnerMixin):
    model = Event
    template_name = root+"event/delete_confirm.html"
    success_url = reverse_lazy("calendar_event:calendar_events")


class EventUpdateView(UpdateView, LoginRequiredMixin, UserIsOwnerMixin):
    model = Event
    template_name = root + "event/update_event.html"
    success_url = reverse_lazy("calendar_event:calendar_events")
    form_class = EventCreateForm

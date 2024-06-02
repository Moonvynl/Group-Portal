from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView, DetailView, DeleteView, UpdateView
from calendar_events.models import Event
from django.utils import timezone
from django.template.defaulttags import register
from calendar_events.events_func import next_date, previous_date, selected_date_events, month_events
from calendar_events.forms import EventCreateForm
from django.utils import timezone
import calendar
import datetime
from auth_system.models import CustomUser


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

    context = {
        "calendar": calendar.Calendar().monthdays2calendar(date.year, date.month),
        "today": timezone.now(),
        "date": date,
        "selected_date_events": selected_date_events(date),
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


class EventCreateView(CreateView):
    model = Event
    template_name = root + "event/create_form.html"
    form_class = EventCreateForm
    success_url = reverse_lazy("calendar_event:calendar_events")

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class EventDeleteView(DeleteView):
    model = Event
    template_name = root+"event/delete_confirm.html"
    success_url = reverse_lazy("calendar_event:calendar_events")


class EventUpdateView(UpdateView):
    model = Event
    template_name = root + "event/update_event.html"
    success_url = reverse_lazy("calendar_event:calendar_events")
    form_class = EventCreateForm

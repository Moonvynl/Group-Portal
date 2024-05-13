from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView, DetailView
from calendar_events.models import Event
from django.utils import timezone
from django.template.defaulttags import register
import calendar
import datetime


def view_date_events(request, day=None, month=None, year=None):
    if not day or not month or not year:
        today = timezone.now()
        date = datetime.datetime(today.year, today.month, today.day)
    else:
        date = datetime.datetime(year, month, day)

    events_date = Event.objects.filter(event_date=date)

    context = {
        "calendar": calendar.Calendar().monthdays2calendar(date.year, date.month),
        "events": Event.objects.all(),
        "date": date,
        "events_date": events_date
    }

    return render(
        template_name="calendar_events/calendar_page.html",
        context=context,
        request=request
    )

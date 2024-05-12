from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView
from calendar_events.models import Event
from django.utils import timezone
from django.template.defaulttags import register
import calendar

class CalendarEventListView(ListView):
    model = Event
    context_object_name = "events"
    template_name = "calendar_events/calendar_page.html"

    def get_context_data(self,*args, **kwargs):
        context = super(CalendarEventListView, self).get_context_data(*args,**kwargs)
        today = timezone.now()
        context['calendar'] = calendar.Calendar().monthdays2calendar(today.year, today.month)
        context['today'] = today
        return context

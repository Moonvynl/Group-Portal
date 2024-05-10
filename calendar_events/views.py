from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView
from calendar_events.models import Event
from calendar import monthrange
from django.utils import timezone
from django.template.defaulttags import register


class CalendarEventListView(ListView):
    model = Event
    context_object_name = "events"
    template_name = "calendar_events/calendar_page.html"

    def get_context_data(self,*args, **kwargs):
        context = super(CalendarEventListView, self).get_context_data(*args,**kwargs)
        today = timezone.now()
        days_of_month = monthrange(today.year, today.month)[1] + 1
        context['days_of_month'] = days_of_month
        return context

from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseBadRequest
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from photo_gallery.models import PhotoPost
from django.utils import timezone
from django.template.defaulttags import register
from django.utils import timezone
from django.core.paginator import Paginator

root = 'photo_gallery/'

class PhotoPostCreateView(CreateView):
    model = PhotoPost
    template_name = root + "event/create_form.html"
    form_class = EventCreateForm
    success_url = reverse_lazy("calendar_event:calendar_events")

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

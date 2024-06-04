from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseBadRequest
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from photo_gallery.models import PhotoPost, PhotoAuth
from django.utils import timezone
from django.template.defaulttags import register
from django.utils import timezone
from django.core.paginator import Paginator
from photo_gallery.forms import PhotoPostForm, PhotoAuthForm

root = 'photo_gallery/'
app_tag = 'photo_post:'

class PhotoPostListView(ListView):
    model = PhotoPost
    template_name = root + 'photo_post/list_view.html'
    context_object_name = 'photo_posts'


class PhotoPostCreateView(CreateView):
    model = PhotoPost
    template_name = root + "photo_post/create_form.html"
    success_url = reverse_lazy(app_tag+"photo_posts")
    form_class = PhotoPostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PhotoAuthCreateView(CreateView):
    model = PhotoAuth
    template_name = root + "confirm_photopost.html"
    success_url = reverse_lazy(app_tag+"photo_posts")
    form_class = PhotoAuthForm
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.authorized = False
        return super().form_valid(form)


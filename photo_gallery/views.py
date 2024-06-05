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
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

root = 'photo_gallery/'
app_tag = 'photo_post:'


@method_decorator(staff_member_required, name='dispatch')
class StaffPostSubmitListView(ListView):
    model = PhotoAuth
    template_name = root + 'staff_submit.html'
    context_object_name = 'auth_requests'


class PhotoUserListView(ListView):
    model = PhotoPost
    template_name = root + 'user_photos.html'
    context_object_name = 'photo_posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photo_posts'] = PhotoPost.objects.filter(author=self.request.user).all()
        return context


class PhotoAuthListView(ListView):
    model = PhotoAuth
    template_name = root + 'photo_post/list_view.html'
    context_object_name = 'photo_posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photo_posts'] = PhotoAuth.objects.filter(status='1').all()
        return context


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

    def get_initial(self):
        initial = super().get_initial()
        initial['pk'] = PhotoAuth.objects.get(id=self.kwargs['pk'])
        return initial


from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseBadRequest
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from photo_gallery.models import PhotoPost, PhotoAuth
from django.template.defaulttags import register
from django.core.paginator import Paginator
from photo_gallery.forms import PhotoPostForm, PhotoAuthForm, PhotoAuthStaffForm
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from photo_gallery.mixins import UserIsOwnerMixin
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin


root = 'photo_gallery/'
app_tag = 'photo_post:'


class PhotoPostLike(UpdateView, LoginRequiredMixin):
    model = PhotoPost

    def get_object(self):
        post_id = self.kwargs.get("pk")
        return get_object_or_404(PhotoPost, pk=post_id)

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        user = request.user
        if user in post.likes.all():
            post.likes.remove(user)
        else:
            post.likes.add(user)
        post.save()
        return HttpResponseRedirect(reverse_lazy("photo_post:photo_posts"))


class PhotoPostDeleteView(DeleteView, UserIsOwnerMixin):
    model = PhotoPost
    template_name = root+"photo_post/delete_confirm.html"
    success_url = reverse_lazy("photo_post:user_photos")


@method_decorator(staff_member_required, name='dispatch')
class StaffPostSubmitListView(ListView):
    model = PhotoAuth
    template_name = root + 'staff_submit.html'
    context_object_name = 'auth_requests'
    paginate_by = 5


@method_decorator(staff_member_required, name='dispatch')
class StaffPostUpdateView(UpdateView):
    model = PhotoAuth
    template_name = root + "staff_auth_form.html"
    success_url = reverse_lazy(app_tag+"post_auth_list")
    form_class = PhotoAuthStaffForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = PhotoAuth.objects.get(id=self.object.id).photo_post
        return context


class PhotoUserListView(ListView):
    model = PhotoPost
    template_name = root + 'user_photos.html'
    context_object_name = 'photo_posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator( PhotoPost.objects.filter(author=self.request.user.id).all(), 5)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['photo_posts'] = page_obj
        return context


class PhotoAuthListView(ListView):
    model = PhotoAuth
    template_name = root + 'photo_post/list_view.html'
    context_object_name = 'photo_posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(PhotoAuth.objects.filter(status='1').all(), 5)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['photo_posts'] = page_obj
        return context


class PhotoPostCreateView(CreateView, LoginRequiredMixin):
    model = PhotoPost
    template_name = root + "photo_post/create_form.html"
    success_url = reverse_lazy(app_tag+"user_photos")
    form_class = PhotoPostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PhotoAuthCreateView(CreateView, LoginRequiredMixin, UserIsOwnerMixin):
    model = PhotoAuth
    template_name = root + "confirm_photopost.html"
    success_url = reverse_lazy(app_tag+"photo_posts")
    form_class = PhotoAuthForm
    
    def form_valid(self, form):
        form.instance.authorized = False
        return super().form_valid(form)

    def get_initial(self):
        initial = super().get_initial()
        initial['pk'] = get_object_or_404(PhotoPost, id=self.kwargs['pk'])
        return initial


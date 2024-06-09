from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, View, UpdateView, DeleteView
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator
from .models import Advert
from .forms import AdvertCreationForm, AdvertUpdateForm


# Create your views here.

class AdvertsListView(ListView):
    model = Advert
    template_name = 'adverts/adverts-list.html'
    context_object_name = 'adverts'
    paginate_by = 10


class AdvertDetailView(DetailView):
    model = Advert
    template_name = 'adverts/advert-detail.html'
    context_object_name = 'advert'


def is_user_admin_or_moderator(user):
    return user.is_authenticated and (user.access == 'moder' or user.is_staff)


@method_decorator(user_passes_test(is_user_admin_or_moderator), name='dispatch')
class AdvertCreateView(View):
    form_class = AdvertCreationForm
    template_name = 'adverts/advert-create.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class

        context = {
            'form': form
        }

        return render(
            request,
            self.template_name,
            context
        )
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        context = {
            'form': form
        }

        if form.is_valid():
            form.instance.author_id = self.request.user.id
            advert = form.save()
            return redirect('adverts:adverts-list')
        
        return render(
            request,
            self.template_name,
            context
        )


@method_decorator(user_passes_test(is_user_admin_or_moderator), name='dispatch')
class AdvertUpdateView(UpdateView):
    model = Advert
    form_class = AdvertUpdateForm
    template_name = 'adverts/advert-update.html'
    success_url = reverse_lazy('adverts:adverts-list')


@method_decorator(user_passes_test(is_user_admin_or_moderator), name='dispatch')
class AdvertDeleteView(DeleteView):
    model = Advert
    template_name = 'adverts/advert-delete.html'
    success_url = reverse_lazy('adverts:adverts-list')
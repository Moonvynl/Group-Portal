from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, View
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from .models import Advert
from .forms import AdvertCreationForm


# Create your views here.

class AdvertsListView(ListView):
    model = Advert
    template_name = 'adverts/adverts-list.html'
    context_object_name = 'adverts'


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
        form = self.form_class(request.POST)

        context = {
            'form': form
        }

        if form.is_valid():
            form.instance.author_id = self.request.user.id
            advert = form.save()
            return redirect('adverts-list')
        
        return render(
            request,
            self.template_name,
            context
        )

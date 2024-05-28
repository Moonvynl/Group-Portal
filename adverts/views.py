from django.shortcuts import render
from django.views.generic import ListView
from .models import Advert


# Create your views here.

class AdvertsListView(ListView):
    model = Advert
    template_name = 'adverts/adverts-list.html'
    context_object_name = 'adverts'
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Advert


# Create your views here.

class AdvertsListView(ListView):
    model = Advert
    template_name = 'adverts/adverts-list.html'
    context_object_name = 'adverts'


class AdvertDetailView(DetailView):
    model = Advert
    template_name = 'adverts/advert-detail.html'
    context_object_name = 'advert'
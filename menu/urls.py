from django.contrib import admin
from django.urls import path
from menu.views import *


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]

app_name = 'menu'
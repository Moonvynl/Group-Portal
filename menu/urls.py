from django.contrib import admin
from django.urls import path
from menu.views import *
app_name = 'menu'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
]


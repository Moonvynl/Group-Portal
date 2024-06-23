from django.urls import path
from . import views

urlpatterns = [
    path('polls', views.index, name = 'index'),
    path('vote/<str:pk>', views.vote, name = 'vote'),
    path('result/<str:pk>', views.result, name = 'result')
]

app_name = 'polls' 
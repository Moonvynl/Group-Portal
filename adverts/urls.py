from django.urls import path
from .views import AdvertsListView


urlpatterns = [
    path('list/', AdvertsListView.as_view(), name='adverts-list'),
]
from django.urls import path
from .views import AdvertsListView, AdvertDetailView, AdvertCreateView, AdvertUpdateView


urlpatterns = [
    path('list/', AdvertsListView.as_view(), name='adverts-list'),
    path('<int:pk>/detail/', AdvertDetailView.as_view(), name='advert-detail'),
    path('create/', AdvertCreateView.as_view(), name='advert-create'),
    path('<int:pk>/update/', AdvertUpdateView.as_view(), name='advert-update'),
]
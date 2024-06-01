from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import AdvertsListView, AdvertDetailView, AdvertCreateView, AdvertUpdateView, AdvertDeleteView


urlpatterns = [
    path('list/', AdvertsListView.as_view(), name='adverts-list'),
    path('<int:pk>/detail/', AdvertDetailView.as_view(), name='advert-detail'),
    path('create/', AdvertCreateView.as_view(), name='advert-create'),
    path('<int:pk>/update/', AdvertUpdateView.as_view(), name='advert-update'),
    path('<int:pk>/delete/', AdvertDeleteView.as_view(), name='advert-delete')
]
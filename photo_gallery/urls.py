from django.urls import path
from django.urls import reverse_lazy
from photo_gallery.views import PhotoPostCreateView, PhotoAuthCreateView, PhotoPostListView

urlpatterns = [
    path('photo_posts/', PhotoPostListView.as_view(), name='photo_posts'),
    path('create_photo/', PhotoPostCreateView.as_view(), name='create_photo'),
    path('auth_request/photopost/', PhotoAuthCreateView.as_view(), name='auth_photo')
]

app_name = 'photo_post'
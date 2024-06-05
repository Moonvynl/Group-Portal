from django.urls import path
from django.urls import reverse_lazy
from photo_gallery.views import PhotoPostCreateView, PhotoAuthCreateView, PhotoAuthListView, PhotoUserListView, StaffPostSubmitListView

urlpatterns = [
    path('photo_posts/', PhotoAuthListView.as_view(), name='photo_posts'),
    path('photo_posts/user/', PhotoUserListView.as_view(), name='user_photos'),
    path('create_photo/', PhotoPostCreateView.as_view(), name='create_photo'),
    path('auth_request/photopost/<int:pk>', PhotoAuthCreateView.as_view(), name='auth_photo'),
    path('post_auth_list/', StaffPostSubmitListView.as_view(), name='post_auth_list'),
]

app_name = 'photo_post'
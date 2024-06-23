from django.urls import path
from .views import *


urlpatterns = [
    path('user-list', UsersList.as_view(), name='user-list'),
    path('profile/<int:pk>/', UserProfile.as_view(), name='profile'),
    path('create-portfolio', CreatePortfolio.as_view(), name='create-portfolio'),
    path('delete-portfolio', DeletePortfolio.as_view(), name='delete-portfolio'),
    path('create-project', CreateProject.as_view(), name='create-project'),
    path('delete-project/<int:pk>/', DeleteProject.as_view(), name='delete-project'),
]

app_name = 'user'

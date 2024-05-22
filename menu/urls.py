from django.contrib import admin
from django.urls import path
from menu.views import *

urlpatterns = [
<<<<<<< HEAD
    path('', IndexView.as_view(), name='index'),
]
app_name = 'menu'
=======
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
>>>>>>> 712ffd0f8bb20fd94e9693589a1f68a41100b19e

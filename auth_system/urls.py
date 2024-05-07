from django.urls import path
from .views import RegisterView, TestTemplateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

urlpatterns = [
    path('login/', LoginView.as_view(template_name='auth_system/login.html' , extra_context={'next': reverse_lazy('auth_system:test')}), name='login' ),
    path('register/', RegisterView.as_view(template_name='auth_system/register.html'), name='register'),
    path('test/', TestTemplateView.as_view(), name='test')
]

app_name = 'auth_system'
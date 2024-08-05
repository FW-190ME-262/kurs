from django.contrib.auth.views import LoginView
from django.urls import path
from django import forms
from .views import home
from . import views
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    # path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('register', views.register, name='register'),
    ]
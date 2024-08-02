from django.contrib.auth.views import LoginView
from django.urls import path
from django import forms
from .views import home
from . import views
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    ]
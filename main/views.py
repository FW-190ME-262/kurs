from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import DetailView
# from .forms import ProductForm
# from .models import Product
from django.shortcuts import redirect
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')

from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import DetailView
# from .forms import ProductForm
# from .models import Product
from django.shortcuts import redirect
from django.http import HttpResponse
from .forms import UserProfileForm
from .models import Profile

def home(request):
    return render(request, 'home.html')




def register(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserProfileForm()
    return render(request, 'register/register.html', {'form': form})

def student_login(request):
    return render(request,'student_login.html')

def teacher_login(request):
    return render(request, 'teacher_login.html')

def proverka(request):
    if Profile.rol == 'role1':
        return render(request,'student_login.html')
    elif Profile.rol == 'role2':
        return render(request,'teacher_login.html')
    else:
        return HttpResponse('Вы не являетесь студентом или учителем')
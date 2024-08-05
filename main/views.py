from django.contrib.auth.decorators import login_required
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
            return redirect('login')
    else:
        form = UserProfileForm()
    return render(request, 'register/register.html', {'form': form})


def teacher_dashboard(request):
    # Код для страницы учителя
    return render(request, 'teacher_dashboard.html')


def student_dashboard(request):
    profile = request.user.profile
    print(profile)
    user = request.user
    print(user)

    return render(request, 'student_dashboard.html', {'user': user, 'profile': profile})


@login_required
def role_redirect(request):
    profile = request.user.profile
    if profile.rol == 'role1':
        return redirect('teacher_dashboard')
    elif profile.rol == 'role2':
        return redirect('student_dashboard')
    else:
        return redirect('другая страница')

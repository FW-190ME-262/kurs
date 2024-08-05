from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django_recaptcha.fields import ReCaptchaField
from django import forms
from .models import Profile

class UserProfileForm(forms.ModelForm):
    recaptcha = ReCaptchaField()
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    bio = forms.CharField(widget=forms.Textarea)


    class Meta:
        model = Profile
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'bio', 'rol', 'recaptcha']


    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            password=self.cleaned_data['password']
        )
        profile = Profile(user=user, bio=self.cleaned_data['bio'], rol=self.cleaned_data['rol'])
        if commit:
            profile.save()
        return profile

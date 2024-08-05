from django.db import models
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    ROLES =[('role1','teacher'),('role2','student')]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    rol = models.CharField(choices=ROLES, max_length=20)

from django.contrib.auth.models import AbstractUser, PermissionsMixin, UserManager
from django.contrib.auth.models import User
from django.db import models


class Director(UserManager):
    pass


class MasterUser(AbstractUser, PermissionsMixin):
    USERNAME_MAX_LENGTH = 15
    FIRST_NAME_MAX_LENGTH = 15
    LAST_NAME_MAX_LENGTH = 15

    username = models.CharField(max_length=USERNAME_MAX_LENGTH, unique=True)
    email = models.EmailField(unique=True)
    date_joined = models.DateField(auto_now_add=True)
    phone_no = models.CharField(max_length=10)
    age = models.PositiveIntegerField()
    first_name = models.CharField(max_length=FIRST_NAME_MAX_LENGTH,)
    last_name = models.CharField(max_length=LAST_NAME_MAX_LENGTH,)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['age', 'first_name', 'last_name']


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 15
    LAST_NAME_MAX_LENGTH = 15

    first_name = models.CharField(max_length=FIRST_NAME_MAX_LENGTH, )
    last_name = models.CharField(max_length=LAST_NAME_MAX_LENGTH, )
    age = models.PositiveIntegerField()
    user = models.OneToOneField(MasterUser, on_delete=models.CASCADE)

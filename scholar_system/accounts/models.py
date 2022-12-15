from django.contrib.auth.models import UserManager, AbstractUser, PermissionsMixin
from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models

from scholar_system.accounts.validators import validate_username, validate_name


class Director(UserManager):
    pass


class MasterUser(AbstractUser, PermissionsMixin):
    USERNAME_MAX_LENGTH = 15
    FIRST_NAME_MAX_LENGTH = 15
    LAST_NAME_MAX_LENGTH = 15

    username = models.CharField(max_length=USERNAME_MAX_LENGTH, unique=True,
                                validators=[MinLengthValidator(4), validate_username, ])

    email = models.EmailField(unique=True)

    date_joined = models.DateField(auto_now_add=True)

    age = models.PositiveIntegerField(validators=[MinValueValidator(14), ])

    first_name = models.CharField(max_length=FIRST_NAME_MAX_LENGTH,
                                  validators=[validate_name, ])

    last_name = models.CharField(max_length=LAST_NAME_MAX_LENGTH,
                                 validators=[validate_name, ])

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'age', 'first_name', 'last_name']

    objects = Director()


class Profile(models.Model):
    USERNAME_MAX_LENGTH = 15
    FIRST_NAME_MAX_LENGTH = 15
    LAST_NAME_MAX_LENGTH = 15

    username = models.CharField(max_length=USERNAME_MAX_LENGTH, unique=True, null=False, default=False,
                                validators=[MinLengthValidator(4), validate_username, ])

    first_name = models.CharField(max_length=FIRST_NAME_MAX_LENGTH,
                                  validators=[validate_name, ])

    last_name = models.CharField(max_length=LAST_NAME_MAX_LENGTH,
                                 validators=[validate_name, ])

    age = models.PositiveIntegerField(validators=[MinValueValidator(18), ])

    user = models.OneToOneField(MasterUser, primary_key=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.username

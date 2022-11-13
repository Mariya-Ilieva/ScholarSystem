from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from scholar_system.accounts.models import MasterUser


@admin.register(MasterUser)
class RegisterMasterUser(UserAdmin):
    model = MasterUser

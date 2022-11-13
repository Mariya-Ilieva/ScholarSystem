from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from scholar_system.accounts.models import MasterUser


@admin.register(MasterUser)
class RegisterMasterUser(UserAdmin):
    model = MasterUser
    list_display = ('username', 'email', 'phone_no', 'is_staff')
    list_filter = ('is_staff',)
    ordering = ('username',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'is_staff', 'is_superuser',
                           'is_verified', 'is_active', 'date_joined', )}),
        ('Permissions', {'fields': ('groups', 'user_permissions'), }),
    )
    add_fieldsets = (
        (None, {'fields': ('username', 'email', 'password1', 'password2'), }),
    )
    readonly_fields = ('date_joined',)

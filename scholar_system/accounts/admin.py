from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from scholar_system.accounts.models import MasterUser, Profile


@admin.register(MasterUser)
class RegisterMasterUser(UserAdmin):
    model = MasterUser
    list_display = ('username', 'email', 'is_staff', 'date_joined')
    list_filter = ('is_staff', )
    ordering = ('-is_superuser', 'username', )
    fieldsets = (
        (None, {'fields': ('email', 'password', 'is_staff', 'is_superuser',
                           'is_active', 'date_joined', )}),
        ('Permissions', {'fields': ('groups', 'user_permissions'), }),
    )
    add_fieldsets = (
        (None, {'fields': ('username', 'email', 'password1', 'password2'), }),
    )
    readonly_fields = ('date_joined',)


@admin.register(Profile)
class RegisterProfile(admin.ModelAdmin):
    list_display = ('username', 'age', 'first_name', 'last_name')

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from scholar_system.accounts.models import MasterUser, Profile


@admin.register(MasterUser)
class RegisterMasterUser(UserAdmin):
    model = MasterUser
    actions = ['activate_staff', 'deactivate_staff']
    list_display = ['username', 'email', 'is_staff', 'date_joined', ]
    list_filter = ['is_staff', ]
    ordering = ['-is_superuser', 'username', ]

    fieldsets = (
        (None, {'fields': ('email', 'password', 'is_staff', 'is_superuser', 'is_active', 'date_joined', )}),
        ('Permissions', {'fields': ('groups', 'user_permissions'), }),
    )

    add_fieldsets = (
        ('Personal', {'fields': (('username', 'age'), 'email', ('first_name', 'last_name'), ('password1', 'password2')), }),
    )

    readonly_fields = ['date_joined', ]
    list_per_page = 15

    def activate_staff(self, request, queryset):
        queryset.update(is_staff=True)

    def deactivate_staff(self, request, queryset):
        queryset.update(is_staff=False)

@admin.register(Profile)
class RegisterProfile(admin.ModelAdmin):
    list_display = ['username', 'age', 'first_name', 'last_name', ]
    list_filter = ['username', ]
    sortable_by = ['age', ]
    search_fields = ['first_name', 'last_name', ]
    list_select_related = ['user', ]
    list_per_page = 15

from django.contrib import admin
from scholar_system.seminars.models import Seminar


@admin.register(Seminar)
class RegisterSeminar(admin.ModelAdmin):
    list_display = ['theme', 'date', 'time', 'link']

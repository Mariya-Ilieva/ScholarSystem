from django.contrib import admin
from django.utils.html import format_html

from scholar_system.seminars.models import Seminar


@admin.register(Seminar)
class RegisterSeminar(admin.ModelAdmin):
    list_display = ['theme', 'date', 'time', 'show_link', ]
    list_filter = ['date', ]
    search_fields = ['theme', 'date', ]
    sortable_by = ['date', ]
    list_per_page = 15

    def show_link(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.link)

from django.utils.html import format_html
from django.contrib import admin

from scholar_system.seminars.models import Seminar


@admin.register(Seminar)
class RegisterSeminar(admin.ModelAdmin):
    list_display = ['theme', 'date', 'time', 'show_link', ]
    list_filter = ['date', ]
    search_fields = ['theme', 'date', ]
    sortable_by = ['date', ]
    list_editable = ['time', ]
    list_per_page = 15

    @staticmethod
    def show_link(obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.link)

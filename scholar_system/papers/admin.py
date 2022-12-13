from django.contrib import admin
from scholar_system.papers.models import Topic, Paper, Comment


@admin.register(Topic)
class RegisterTopic(admin.ModelAdmin):
    list_display = ['title', ]
    search_fields = ['title', ]
    list_filter = ['title', ]
    list_per_page = 20


@admin.register(Paper)
class RegisterPaper(admin.ModelAdmin):
    list_display = ['topic', 'less_description', 'created_by', 'publication_date', ]
    list_filter = ['publication_date', 'topic', ]
    search_fields = ['topic', 'created_by', ]
    sortable_by = ['publication_date', ]
    list_select_related = ['topic', 'created_by', ]
    list_per_page = 10

    def less_description(self, obj):
        return f'{obj.description[:200]}...'


@admin.register(Comment)
class RegisterComment(admin.ModelAdmin):
    list_display = ['paper', 'text', 'commented_by', 'publication_datetime', ]
    list_filter = ['paper', ]
    search_fields = ['commented_by', ]
    sortable_by = ['publication_datetime', ]
    list_select_related = ['paper', 'commented_by', ]
    list_per_page = 10

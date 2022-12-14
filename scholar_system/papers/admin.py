from django.contrib import admin
from scholar_system.papers.models import Topic, Paper, Comment


class PaperInline(admin.StackedInline):
    model = Paper
    extra = 1


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


@admin.register(Topic)
class RegisterTopic(admin.ModelAdmin):
    list_display = ['title', ]
    search_fields = ['title', ]
    list_filter = ['title', ]
    inlines = [PaperInline]
    list_per_page = 20


@admin.register(Paper)
class RegisterPaper(admin.ModelAdmin):
    list_display = ['topic', 'short_description', 'created_by', 'publication_date', ]
    date_hierarchy = 'publication_date'
    list_filter = ['publication_date', 'topic', ]
    search_fields = ['topic', 'created_by', ]
    sortable_by = ['publication_date', ]
    list_select_related = ['topic', 'created_by', ]
    inlines = [CommentInline]
    list_per_page = 15

    def short_description(self, obj):
        return f'{obj.description[:200]}...'


@admin.register(Comment)
class RegisterComment(admin.ModelAdmin):
    list_display = ['paper', 'text', 'commented_by', 'publication_datetime', ]
    date_hierarchy = 'publication_datetime'
    list_filter = ['paper', ]
    search_fields = ['commented_by', ]
    sortable_by = ['publication_datetime', ]
    list_select_related = ['paper', 'commented_by', ]
    list_per_page = 15

from django.contrib import admin
from scholar_system.papers.models import Topic, Paper, Comment


@admin.register(Topic)
class RegisterTopic(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Paper)
class RegisterPaper(admin.ModelAdmin):
    list_display = ['topic', 'created_by']


@admin.register(Comment)
class RegisterComment(admin.ModelAdmin):
    list_display = ['commented_by']

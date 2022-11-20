from django import forms
from scholar_system.papers.models import Topic


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ('title', )

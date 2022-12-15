from django.forms import ModelForm

from scholar_system.papers.models import Topic


class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ['title', ]

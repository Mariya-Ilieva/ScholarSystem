from django import forms
from scholar_system.papers.models import Topic


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ('title', )


class DeleteTopicForm(TopicForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.keys():
            self.fields[field].disabled = True

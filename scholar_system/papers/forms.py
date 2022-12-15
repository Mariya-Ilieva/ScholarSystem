from django.forms import ModelForm

from scholar_system.papers.models import Paper, Comment


class PaperForm(ModelForm):
    class Meta:
        model = Paper
        fields = ['topic', 'description', ]


class CreatePaperForm(PaperForm):
    class Meta(PaperForm.Meta):
        pass


class EditPaperForm(PaperForm):
    class Meta(PaperForm.Meta):
        pass


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text', ]


class CreateCommentForm(CommentForm):
    class Meta(CommentForm.Meta):
        pass


class EditCommentForm(CommentForm):
    class Meta(CommentForm.Meta):
        pass

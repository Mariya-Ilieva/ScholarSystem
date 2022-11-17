from django import forms
from scholar_system.papers.models import Paper, Comment


class PaperForm(forms.ModelForm):
    class Meta:
        model = Paper
        fields = ('topic', 'description')


class CreatePaperForm(PaperForm):
    class Meta(PaperForm.Meta):
        pass


class EditPaperForm(PaperForm):
    class Meta(PaperForm.Meta):
        pass


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', )


class CreateCommentForm(CommentForm):
    class Meta(CommentForm.Meta):
        pass


class EditCommentForm(CommentForm):
    class Meta(CommentForm.Meta):
        pass

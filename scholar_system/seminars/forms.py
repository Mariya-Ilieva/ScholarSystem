from django import forms
from scholar_system.seminars.models import Seminar


class SeminarForm(forms.ModelForm):
    class Meta:
        model = Seminar
        fields = '__all__'

from django import forms
from django.forms import ModelForm

from scholar_system.seminars.models import Seminar


class SeminarForm(ModelForm):
    class Meta:
        model = Seminar
        fields = '__all__'
        widgets = {
            'date': forms.SelectDateWidget()
        }

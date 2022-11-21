from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic


class CreateSeminarView(LoginRequiredMixin, generic.CreateView):
    pass


class DetailsSeminarView(LoginRequiredMixin, generic.UpdateView):
    pass


class EditSeminarView(LoginRequiredMixin, generic.UpdateView):
    pass


class DeleteSeminarView(LoginRequiredMixin, generic.DeleteView):
    pass

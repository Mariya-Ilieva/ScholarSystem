from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from scholar_system.seminars.forms import SeminarForm
from scholar_system.seminars.models import Seminar


class CreateSeminarView(LoginRequiredMixin, generic.CreateView):
    model = Seminar
    form_class = SeminarForm
    template_name = 'seminar/add_seminar.html'
    success_url = reverse_lazy('all seminars')


class DetailsSeminarView(LoginRequiredMixin, generic.DetailView):
    model = Seminar
    form_class = SeminarForm
    template_name = 'seminar/details_seminar.html'


class EditSeminarView(LoginRequiredMixin, generic.UpdateView):
    model = Seminar
    form_class = SeminarForm
    template_name = 'seminar/edit_seminar.html'
    success_url = reverse_lazy('all seminars')

    def get_success_url(self):
        seminar_id = self.object.id
        return reverse('seminar details', kwargs={'pk': seminar_id})


class DeleteSeminarView(LoginRequiredMixin, generic.DeleteView):
    model = Seminar
    template_name = 'seminar/delete_seminar.html'
    success_url = reverse_lazy('all seminars')


class AllSeminarsView(generic.ListView):
    model = Seminar
    template_name = 'seminar/all_seminars.html'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['seminar_list'] = Seminar.objects.all()
        return context

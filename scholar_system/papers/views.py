from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from textwrap import wrap

from django.http import FileResponse
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from scholar_system.accounts.models import Profile
from scholar_system.papers.models import Paper, Comment
from scholar_system.papers.forms import PaperForm, CreatePaperForm, EditPaperForm, CreateCommentForm, EditCommentForm
from scholar_system.papers.utils import is_owner


class UserPapersView(ListView):
    model = Paper
    template_name = 'paper/my_papers.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(pk=self.request.user.id)
        context['user_papers'] = Paper.objects.filter(created_by=profile)
        return context


class CreatePaperView(LoginRequiredMixin, CreateView):
    model = Paper
    form_class = CreatePaperForm
    template_name = 'paper/add_paper.html'
    success_url = reverse_lazy('papers user')

    def form_valid(self, form):
        user = Profile.objects.get(pk=self.request.user.id)
        form.instance.created_by = user
        form.save()
        return super().form_valid(form)


class DetailsPaperView(LoginRequiredMixin, DetailView):
    model = Paper
    form_class = PaperForm
    template_name = 'paper/details_paper.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = False
        context['comments'] = Comment.objects.filter(paper_id=self.object.id)
        if self.request.user.is_authenticated:
            profile = Profile.objects.get(pk=self.request.user.id)
            context['is_owner'] = context['object'].created_by == profile
            context['profile'] = profile
        return context


class EditPaperView(LoginRequiredMixin, UpdateView):
    model = Paper
    form_class = EditPaperForm
    template_name = 'paper/edit_paper.html'
    success_url = reverse_lazy('papers user')

    def get_success_url(self):
        paper_id = self.object.id
        return reverse('paper details', kwargs={'pk': paper_id})

    def dispatch(self, request, *args, **kwargs):
        paper = Paper.objects.get(pk=kwargs['pk'])
        if not is_owner(self.request, paper.created_by):
            return redirect('unauthorized')
        return super().dispatch(request, *args, **kwargs)


class DeletePaperView(LoginRequiredMixin, DeleteView):
    model = Paper
    template_name = 'paper/delete_paper.html'
    success_url = reverse_lazy('papers user')

    def dispatch(self, request, *args, **kwargs):
        paper = Paper.objects.get(pk=kwargs['pk'])
        if not is_owner(self.request, paper.created_by):
            return redirect('unauthorized')
        return super().dispatch(request, *args, **kwargs)


class AddCommentView(LoginRequiredMixin, CreateView):
    form_class = CreateCommentForm
    template_name = 'comment/add_comment.html'
    success_url = reverse_lazy('home page')

    def post(self, request, *args, **kwargs):
        text = self.request.POST['text']
        user = Profile.objects.get(user_id=self.request.user.id)
        path = self.request.path.split('/')
        paper_id = path[2].replace('int:', '')
        paper = Paper.objects.get(pk=paper_id)
        comment = Comment(
            text=text,
            paper_id=paper.id,
            commented_by=user,
        )
        comment.save()

        url = reverse('paper details', kwargs={'pk': paper_id})
        return redirect(url)


class EditCommentView(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = EditCommentForm
    template_name = 'comment/edit_comment.html'

    def get_success_url(self):
        paper_id = Paper.objects.get(pk=self.object.paper.id).id
        return reverse('paper details', kwargs={'pk': paper_id})

    def dispatch(self, request, *args, **kwargs):
        comment = Comment.objects.get(pk=kwargs['pk'])
        if not is_owner(request, comment.commented_by):
            return redirect('unauthorized')
        return super().dispatch(request, *args, **kwargs)


class DeleteCommentView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'comment/delete_comment.html'

    def get_success_url(self):
        paper_id = Paper.objects.get(pk=self.object.paper.id).id
        return reverse('paper details', kwargs={'pk': paper_id})

    def dispatch(self, request, *args, **kwargs):
        comment = Comment.objects.get(pk=kwargs['pk'])
        if not is_owner(self.request, comment.commented_by):
            return redirect('unauthorized')
        return super().dispatch(request, *args, **kwargs)


def generate_pdf(request, pk):
    path = request.path.split('/')
    paper_id = path[2].replace('int:', '')
    paper = Paper.objects.get(pk=paper_id)
    data = [f'{paper.topic}', f'{paper.description}']

    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter, bottomup=0)
    p.setFont('Helvetica', 18)
    p.drawCentredString(300, 35, data[0])

    text_obj = p.beginText(55, 80)
    text_obj.setFont('Helvetica', 14)

    wrapped_text = '\n'.join(wrap(data[1], 80))
    text_obj.textLines(wrapped_text)

    p.drawText(text_obj)
    p.showPage()
    p.save()
    buffer.seek(0)

    return FileResponse(buffer, as_attachment=False, filename='paper.pdf')

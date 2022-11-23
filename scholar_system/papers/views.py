from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from scholar_system.accounts.models import Profile
from scholar_system.papers.forms import PaperForm, CreatePaperForm, EditPaperForm, CreateCommentForm, EditCommentForm
from scholar_system.papers.models import Paper, Comment
from scholar_system.papers.utils import is_owner


class UserPapersView(generic.ListView):
    model = Paper
    template_name = 'paper/my_papers.html'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(pk=self.request.user.id)
        context['user_papers'] = Paper.objects.filter(created_by=profile)
        return context


class CreatePaperView(LoginRequiredMixin, generic.CreateView):
    model = Paper
    form_class = CreatePaperForm
    template_name = 'paper/add_paper.html'
    success_url = reverse_lazy('papers user')

    def form_valid(self, form):
        user = Profile.objects.get(pk=self.request.user.id)
        form.instance.created_by = user
        form.save()
        return super().form_valid(form)


class DetailsPaperView(LoginRequiredMixin, generic.DetailView):
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


class EditPaperView(LoginRequiredMixin, generic.UpdateView):
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


class DeletePaperView(LoginRequiredMixin, generic.DeleteView):
    model = Paper
    template_name = 'paper/delete_paper.html'
    success_url = reverse_lazy('papers user')

    def dispatch(self, request, *args, **kwargs):
        paper = Paper.objects.get(pk=kwargs['pk'])
        if not is_owner(self.request, paper.created_by):
            return redirect('unauthorized')
        return super().dispatch(request, *args, **kwargs)


class AddCommentView(LoginRequiredMixin, generic.CreateView):
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


class EditCommentView(LoginRequiredMixin, generic.UpdateView):
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


class DeleteCommentView(LoginRequiredMixin, generic.DeleteView):
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

from django.shortcuts import render
from django.views import generic
from scholar_system.papers.models import Paper


def home_page(request):
    return render(request, 'home_page.html')


def unauthorized(request):
    return render(request, 'main/unauthorized.html')


def bad_request(request, exception=None):
    return render(request, 'main/bad_request.html')


def permission_denied(request, exception=None):
    return render(request, 'main/permission_denied.html')


def page_not_found(request, exception=None):
    return render(request, 'main/not_found.html')


def server_error(request, exception=None):
    return render(request, 'main/server_error.html')


class AllPapersView(generic.ListView):
    model = Paper
    template_name = 'all_papers.html'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Paper.objects.all()
        return context

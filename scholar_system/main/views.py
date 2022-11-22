from django.shortcuts import render, redirect
from django.views import generic
from scholar_system.main.forms import TopicForm
from scholar_system.papers.models import Paper, Topic


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
        context['paper_list'] = Paper.objects.all()
        return context


class AllTopicPapersView(generic.ListView):
    paginate_by = 5
    model = Paper
    template_name = 'main/topic_papers.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        path = self.request.path.split('/')
        topic_id = path[2].replace('int:', '')
        topic = Topic.objects.get(pk=topic_id)
        context['topic_papers'] = Paper.objects.filter(topic=topic)
        return context


class AllTopicsView(generic.ListView):
    model = Topic
    template_name = 'topic/all_topics.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['topic_list'] = Topic.objects.all()
        return context


def search_bar(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        paper = Paper.objects.filter(description__icontains=searched)
        context = {
            'searched': searched,
            'paper': paper,
        }
        return render(request, 'search_bar.html', context)
    else:
        return render(request, 'search_bar.html')


def add_topic(request):
    form = TopicForm()
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all topics')
    context = {
        'form': form,
    }
    return render(request, 'topic/add_topic.html', context)


def edit_topic(request, pk):
    topic = Topic.objects.get(pk=pk)
    form = TopicForm(instance=topic)
    if request.method == 'POST':
        form = TopicForm(request.POST, instance=topic)
        if form.is_valid():
            form.save()
            return redirect('all topics')
    context = {
        'form': form,
    }
    return render(request, 'topic/edit_topic.html', context)

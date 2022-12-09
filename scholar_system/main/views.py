from django.shortcuts import render, redirect
from django.views.generic import ListView
from scholar_system.main.forms import TopicForm
from scholar_system.papers.models import Paper, Topic


def home_page(request):
    return render(request, 'home_page.html')


def unauthorized(request):
    return render(request, 'main/unauthorized.html')


def bad_request(request, exception=None):
    return render(request, 'main/bad_request.html', status=400)


def permission_denied(request, exception=None):
    return render(request, 'main/permission_denied.html', status=403)


def page_not_found(request, exception=None):
    return render(request, 'main/not_found.html', status=404)


def server_error(request, exception=None):
    return render(request, 'main/server_error.html', status=500)


class AllPapersView(ListView):
    model = Paper
    template_name = 'all_papers.html'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['paper_list'] = Paper.objects.all()
        return context


class AllTopicPapersView(ListView):
    model = Paper
    template_name = 'main/topic_papers.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        path = self.request.path.split('/')
        topic_id = path[2].replace('int:', '')
        topic = Topic.objects.get(pk=topic_id)
        context['topic'] = topic
        context['topic_papers'] = Paper.objects.filter(topic=topic)
        return context


class AllTopicsView(ListView):
    model = Topic
    template_name = 'topic/all_topics.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['topic_list'] = Topic.objects.all()
        return context


def search_bar(request):
    user_id = request.user.id
    if user_id:
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
    else:
        return redirect(unauthorized)


def add_topic(request):
    form = TopicForm()
    user_id = request.user.id
    if user_id:
        if request.method == 'POST':
            form = TopicForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('all topics')
        context = {
            'form': form,
        }
        return render(request, 'topic/add_topic.html', context)
    else:
        return redirect(unauthorized)


def edit_topic(request, pk):
    topic = Topic.objects.get(pk=pk)
    form = TopicForm(instance=topic)
    user_id = request.user.id
    if user_id:
        if request.method == 'POST':
            form = TopicForm(request.POST, instance=topic)
            if form.is_valid():
                form.save()
                return redirect('all topics')
        context = {
            'form': form,
        }
        return render(request, 'topic/edit_topic.html', context)
    else:
        return redirect(unauthorized)


def delete_topic(request, pk):
    topic = Topic.objects.get(pk=pk)
    user_id = request.user.id
    if user_id:
        if request.method == 'POST':
            topic.delete()
            return redirect('all topics')
        return render(request, 'topic/delete_topic.html')
    else:
        return redirect(unauthorized)

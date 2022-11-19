from django.urls import path, include
from scholar_system.main.views import home_page, unauthorized, AllPapersView, \
    AllTopicsView, add_topic, edit_topic, delete_topic

urlpatterns = [
    path('', home_page, name='home page'),
    path('unauthorized', unauthorized, name='unauthorized'),
    path('all', AllPapersView.as_view(), name='all papers'),
    path('topic/', include([
        path('all/', AllTopicsView.as_view(), name='all topics'),
        path('', add_topic, name='topic add'),
        path('<int:pk>/edit/', edit_topic, name='topic edit'),
        path('<int:pk>/delete/', delete_topic, name='topic delete'),
    ])),
]

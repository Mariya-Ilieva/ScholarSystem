from django.urls import path, include
from scholar_system.main.views import home_page, unauthorized, AllPapersView, AllTopicsView, \
    AllTopicPapersView, search_bar, add_topic, edit_topic, delete_topic

urlpatterns = [
    path('', home_page, name='home page'),
    path('unauthorized', unauthorized, name='unauthorized'),
    path('all-papers', AllPapersView.as_view(), name='all papers'),
    path('search/', search_bar, name='search'),
    path('topic/', include([
        path('all/', AllTopicsView.as_view(), name='all topics'),
        path('', add_topic, name='topic add'),
        path('<int:pk>/', include([
            path('papers/', AllTopicPapersView.as_view(), name='all topic papers'),
            path('edit/', edit_topic, name='topic edit'),
            path('delete/', delete_topic, name='topic delete'),
        ])),
    ])),
]

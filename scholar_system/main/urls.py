from django.urls import path
from scholar_system.main.views import home_page, unauthorized, AllPapersView

urlpatterns = [
    path('', home_page, name='home page'),
    path('unauthorized', unauthorized, name='unauthorized'),
    path('all', AllPapersView.as_view(), name='all papers'),
]

from django.urls import path
from scholar_system.main.views import home_page, unauthorized, handler404, handler500

urlpatterns = [
    path('', home_page, name='home page'),
    path('unauthorized', unauthorized, name='unauthorized'),
    path('404', handler404, name='not found'),
    path('500', handler500, name='server error'),
]

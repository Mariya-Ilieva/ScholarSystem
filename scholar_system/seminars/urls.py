from django.urls import path, include
from scholar_system.seminars.views import CreateSeminarView, DetailsSeminarView, EditSeminarView, DeleteSeminarView


urlpatterns = [
    path('create/', CreateSeminarView.as_view(), name='seminar create'),
    path('<int:pk>/', include([
        path('details/', DetailsSeminarView.as_view(), name='seminar details'),
        path('edit/', EditSeminarView.as_view(), name='seminar edit'),
        path('delete/', DeleteSeminarView.as_view(), name='seminar delete'),
        ])),
    ]

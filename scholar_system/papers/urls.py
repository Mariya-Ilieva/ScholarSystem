from django.urls import path, include
from scholar_system.papers.views import UserPapersView, CreatePaperView, DetailsPaperView, EditPaperView, \
    DeletePaperView, AddCommentView, EditCommentView, DeleteCommentView, generate_pdf

urlpatterns = [
    path('my-papers/', UserPapersView.as_view(), name='papers user'),
    path('create/', CreatePaperView.as_view(), name='paper create'),
    path('<int:pk>/', include([
        path('edit/', EditPaperView.as_view(), name='paper edit'),
        path('delete/', DeletePaperView.as_view(), name='paper delete'),
        path('details/', include([
            path('', DetailsPaperView.as_view(), name='paper details'),
            path('pdf/', generate_pdf, name='generate pdf'),
            path('comment/', include([
                path('', AddCommentView.as_view(), name='comment add'),
                path('edit/', EditCommentView.as_view(), name='comment edit'),
                path('delete/', DeleteCommentView.as_view(), name='comment delete'),
            ])),
        ])),
    ])),
]

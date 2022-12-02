from django.urls import path
from scholar_system.users_API.views import UserListView, UserDetailView

urlpatterns = [
    path('', UserListView.as_view(), name='users'),
    path('<int:pk>/', UserDetailView.as_view()),
]

from django.urls import path

from scholar_system.users_API.views import UserListView, UserDetailDeleteView

urlpatterns = [
    path('', UserListView.as_view(), name='users'),
    path('<int:pk>/', UserDetailDeleteView.as_view(), name='User details'),
]

from django.urls import path
from scholar_system.users_API.views import UserListCreateView, UserUpdateDestroyView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='users'),
    path('<int:pk>/', UserUpdateDestroyView.as_view()),
]

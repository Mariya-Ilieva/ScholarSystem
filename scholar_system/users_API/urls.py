from django.urls import path
from scholar_system.users_API.views import AllUsersAPIView, DetailsUserAPIView

urlpatterns = [
    path('', AllUsersAPIView.as_view(), name='users'),
    path('<int:id>/', DetailsUserAPIView.as_view()),
]

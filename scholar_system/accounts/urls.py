from django.urls import path, include

from scholar_system.accounts.views import RegisterUserView, LoginUserView, LogoutUserView,\
    DetailsUserView, EditUserView, DeleteUserView, ChangePasswordView


urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='user register'),
    path('login/', LoginUserView.as_view(), name='user login'),
    path('logout/', LogoutUserView.as_view(), name='user logout'),
    path('profile/<int:pk>/', include([
            path('details/', DetailsUserView.as_view(), name='user details'),
            path('edit/', EditUserView.as_view(), name='user edit'),
            path('delete/', DeleteUserView.as_view(), name='user delete'),
            path('change-password/', ChangePasswordView.as_view(), name='change password'),
    ]))
]

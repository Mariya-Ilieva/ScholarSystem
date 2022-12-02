from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import View, CreateView, DetailView, UpdateView, DeleteView
from scholar_system.accounts.forms import RegisterUserForm, ChangePasswordForm
from scholar_system.accounts.models import Profile

UserModel = get_user_model()


class CustomPermissionMixin(View):
    def dispatch(self, request, *args, **kwargs):
        user = UserModel.objects.get(pk=kwargs['pk'])
        if request.user != user:
            return redirect('unauthorized')
        return super().dispatch(request, *args, **kwargs)


class RegisterUserView(CreateView):
    form_class = RegisterUserForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('home page')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class LoginUserView(LoginView):
    template_name = 'user/login.html'
    success_url = reverse_lazy('home page')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().success_url


class LogoutUserView(LogoutView):
    next_page = reverse_lazy('home page')


class DetailsUserView(CustomPermissionMixin, DetailView):
    model = Profile
    template_name = 'user/details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(pk=self.object.user.id)
        context['profile'] = profile
        return context


class EditUserView(CustomPermissionMixin, UpdateView):
    model = Profile
    template_name = 'user/edit.html'
    fields = ['username', 'age', 'first_name', 'last_name']

    def form_valid(self, form):
        user = self.request.user
        user.username = form.data.get('username')
        user.age = form.data.get('age')
        user.first_name = form.data.get('first_name')
        user.last_name = form.data.get('last_name')
        user.save()
        return super().form_valid(form)

    def get_success_url(self):
        user_id = self.request.user.pk
        return reverse_lazy('user details', kwargs={'pk': user_id})


class DeleteUserView(CustomPermissionMixin, DeleteView):
    model = UserModel
    template_name = 'user/delete.html'
    success_url = reverse_lazy('home page')


class ChangePasswordView(CustomPermissionMixin, UpdateView):
    model = UserModel
    form_class = ChangePasswordForm
    template_name = 'user/change_password.html'
    success_url = reverse_lazy('user login')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        kwargs.pop('instance')
        return kwargs

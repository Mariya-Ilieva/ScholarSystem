from django.contrib.auth import views, get_user_model
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from scholar_system.accounts.forms import RegisterUserForm, ChangePasswordForm
from scholar_system.accounts.models import Profile, MasterUser

UserModel = get_user_model()


class CustomPermissionMixin(generic.View):
    def dispatch(self, request, *args, **kwargs):
        user = UserModel.objects.get(pk=kwargs['pk'])
        if request.user != user:
            return redirect('unauthorized')
        return super().dispatch(request, *args, **kwargs)


class RegisterUserView(generic.CreateView):
    model = MasterUser
    form_class = RegisterUserForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('user login')


class LoginUserView(views.LoginView):
    template_name = 'user/login.html'
    success_url = reverse_lazy('home page')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().success_url


class LogoutUserView(views.LogoutView):
    next_page = reverse_lazy('home page')


class DetailsUserView(CustomPermissionMixin, generic.DetailView):
    TEMPLATE_NAME = 'Profile Details'
    model = Profile
    template_name = 'user/details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.object.user
        profile = Profile.objects.get(pk=user.id)
        context['profile'] = profile
        context['template_name'] = self.TEMPLATE_NAME
        return context


class EditUserView(CustomPermissionMixin, generic.UpdateView):
    TEMPLATE_NAME = 'Edit Profile'
    model = Profile
    template_name = 'user/edit.html'
    success_url = reverse_lazy('home page')
    fields = ['username', 'age', 'first_name', 'last_name']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['template_name'] = self.TEMPLATE_NAME
        return context


class DeleteUserView(CustomPermissionMixin, generic.DeleteView):
    TEMPLATE_NAME = 'Delete Profile'
    model = MasterUser
    template_name = 'user/delete.html'
    success_url = reverse_lazy('home page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['template_name'] = self.TEMPLATE_NAME
        return context


class ChangePasswordView(CustomPermissionMixin, generic.UpdateView):
    TEMPLATE_NAME = 'Change Password'
    model = UserModel
    form_class = ChangePasswordForm
    fields = '__all__'
    template_name = 'user/change_password.html'
    success_url = reverse_lazy('home page')

    def get_form_class(self):
        return self.form_class

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        kwargs.pop('instance')
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['template_name'] = self.TEMPLATE_NAME
        return context

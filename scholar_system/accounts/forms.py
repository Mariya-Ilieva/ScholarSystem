from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm

from scholar_system.accounts.models import Profile

UserModel = get_user_model()


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['username', 'email', 'age', 'first_name', 'last_name']

    def clean_first_name(self):
        return self.cleaned_data['first_name']

    def clean_last_name(self):
        return self.cleaned_data['last_name']

    def save(self, commit=True):
        user = UserModel(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            age=self.cleaned_data['age'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
        )
        user.set_password(self.cleaned_data['password1'])
        user.save()

        profile = Profile(
            username=self.cleaned_data['username'],
            age=self.cleaned_data['age'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            user=user,
        )
        profile.save()

        return user


class ChangePasswordForm(PasswordChangeForm):
    class Meta:
        model = UserModel
        fields = '__all__'

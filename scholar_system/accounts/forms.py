from django.contrib.auth import forms, get_user_model
from scholar_system.accounts.models import MasterUser, Profile

UserModel = get_user_model()


class RegisterUserForm(forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email', 'first_name', 'last_name')

    def clean_first_name(self):
        return self.cleaned_data['first_name']

    def clean_last_name(self):
        return self.cleaned_data['last_name']

    def save(self, commit=True):
        user = UserModel(
            email=self.cleaned_data['email'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
        )
        user.set_password(self.cleaned_data['password1'])
        user.save()
        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            user=user,
        )
        profile.save()

        return user


class ChangePasswordForm(forms.PasswordChangeForm):
    class Meta:
        model = UserModel
        fields = '__all__'

from scholar_system.accounts.models import Profile


def is_owner(request, obj):
    if request.user == obj.user:
        profile = Profile.objects.get(pk=obj.user.id)
        return profile

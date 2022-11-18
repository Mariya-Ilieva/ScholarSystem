from django import template

register = template.Library()


@register.filter('has_permission')
def has_permission(user, group):
    return user.groups.filter(group).exists()


@register.filter('show_less')
def show_less(text):
    if len(text) > 300:
        return text[:300]

from django import template

register = template.Library()


@register.filter('has_permission')
def has_permission(user, group):
    return user.groups.filter(group).exists()

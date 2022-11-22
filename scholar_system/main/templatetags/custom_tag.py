from django import template

register = template.Library()


@register.filter('show_less')
def show_less(text):
    if len(text) > 300:
        return text[:300]
    return text

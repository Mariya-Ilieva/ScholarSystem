from django import template

register = template.Library()


@register.filter('show_less')
def show_less(text):
    if len(text) > 255:
        return text[:255]
    return text

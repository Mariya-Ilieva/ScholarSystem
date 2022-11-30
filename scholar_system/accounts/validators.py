from django.core.exceptions import ValidationError


def validate_username(value):
    value = value.replace('_', '')
    if not value.isalnum():
        raise ValidationError('Please ensure this username contains only letters, numbers, and underscore.')


def validate_name(value):
    if not value.isalpha():
        raise ValidationError('Please ensure this name contains only letters.')

from datetime import date
from django.core.exceptions import ValidationError


def validate_theme(value):
    if not all(x.isalpha() or x == ' ' for x in value):
        raise ValidationError('Please ensure this theme contains only letters.')


def validate_future_date(value):
    if value < date.today():
        raise ValidationError('Please enter a valid date for the seminar.')

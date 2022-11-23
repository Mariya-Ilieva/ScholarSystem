from datetime import date
from django.core.exceptions import ValidationError


def validate_future_date(value):
    if value < date.today():
        raise ValidationError('Please enter a valid date for the seminar.')

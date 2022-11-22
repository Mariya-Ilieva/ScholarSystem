from datetime import date
from django.core.exceptions import ValidationError


def validate_future_date(value):
    today = date.today()
    if value < today:
        raise ValidationError('Please enter a valid date for the seminar.')

from datetime import date

from django.db import models

from scholar_system.seminars.validators import validate_future_date, validate_theme


class Seminar(models.Model):
    THEME_MAX_LENGTH = 100
    LINK_MAX_LENGTH = 200

    theme = models.CharField(max_length=THEME_MAX_LENGTH, validators=[validate_theme, ])

    date = models.DateField(validators=[validate_future_date, ])

    time = models.TimeField()

    link = models.URLField(max_length=LINK_MAX_LENGTH)

    class Meta:
        ordering = ['date']

    @property
    def days_till(self):
        today = date.today()
        days_till = str(self.date - today).split(',')[0]
        if ':' in days_till:
            result = '0'
        elif days_till.startswith('-'):
            result = f'Event passed {days_till[1::]} ago'
        else:
            result = days_till
        return result

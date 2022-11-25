from datetime import date
from django.db import models
from scholar_system.seminars.validators import validate_future_date


class Seminar(models.Model):
    theme = models.CharField(max_length=100)
    date = models.DateField(validators=[validate_future_date, ])
    time = models.TimeField()
    link = models.URLField(max_length=200)

    @property
    def days_till(self):
        today = date.today()
        days_till = str(self.date - today).split(',')[0]
        return days_till if ':' not in days_till else '0'

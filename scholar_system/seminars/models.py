from django.db import models
from scholar_system.seminars.validators import validate_future_date


class Seminar(models.Model):
    theme = models.CharField(max_length=100)
    date = models.DateField(validators=[validate_future_date, ])
    time = models.TimeField()
    link = models.URLField(max_length=200)

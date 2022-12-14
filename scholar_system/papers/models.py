from django.db import models

from scholar_system.accounts.models import Profile
from scholar_system.seminars.validators import validate_theme


class Topic(models.Model):
    TOPIC_TITLE_MAX_LENGTH = 25

    title = models.CharField(max_length=TOPIC_TITLE_MAX_LENGTH, unique=True,
                             validators=[validate_theme, ])

    def __str__(self):
        return self.title


class Paper(models.Model):
    DESCRIPTION_MAX_LENGTH = 3000

    description = models.TextField(max_length=DESCRIPTION_MAX_LENGTH)

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE,)

    publication_date = models.DateField(auto_now=True, null=False, blank=True, )

    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-publication_date']

    def __str__(self):
        return f'{self.topic} -{self.id}-'


class Comment(models.Model):

    text = models.TextField()

    commented_by = models.ForeignKey(Profile, on_delete=models.CASCADE)

    paper = models.ForeignKey(Paper, on_delete=models.CASCADE)

    publication_datetime = models.DateTimeField(auto_now_add=True, null=False, blank=True, )

    def __str__(self):
        return f'By {self.commented_by}'

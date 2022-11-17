from django.db import models
from scholar_system.accounts.models import Profile


class Topic(models.Model):
    TOPIC_TITLE_MAX_LENGTH = 25

    title = models.CharField(max_length=TOPIC_TITLE_MAX_LENGTH, unique=True, )

    def __str__(self):
        return self.title


class Paper(models.Model):
    description = models.TextField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE,)
    publication_date = models.DateField(auto_now=True, null=False, blank=True, )
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.TextField()
    commented_by = models.ForeignKey(Profile, on_delete=models.CASCADE)
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE)
    publication_datetime = models.DateTimeField(auto_now_add=True, null=False, blank=True, )

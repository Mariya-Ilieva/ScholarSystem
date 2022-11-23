from datetime import date
from django.db.models.signals import post_save
from django.dispatch import receiver
from scholar_system.seminars.models import Seminar


@receiver(post_save, sender=Seminar)
def delete_after_passed(sender, instance, created, **kwargs):
    if created:
        while instance.date >= date.today():
            pass
        else:
            instance.delete()

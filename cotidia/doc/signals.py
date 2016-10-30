from django.dispatch import receiver
from django.db.models.signals import post_save

from cotidia.doc.models import Document


@receiver(post_save, sender=Document)
def doc_update(sender, instance, created, **kwargs):
    pass

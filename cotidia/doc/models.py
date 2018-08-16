import uuid

from django.db import models


class Document(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    body = models.TextField(blank=True)

    is_private = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'

    def __str__(self):
        return self.title

import uuid

from django.conf import settings
from django.db import models


class Notice(models.Model):
    uuid = models.UUIDField(unique=True)
    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='notices', on_delete=models.CASCADE
    )
    body = models.TextField()

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.uuid = str(uuid.uuid4())
        super().save(*args, **kwargs)

    def __str__(self):
        return self.body
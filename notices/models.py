import uuid
from urllib.parse import urljoin

import qrcode
from django.conf import settings
from django.db import models
from PIL.Image import Image


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

    @property
    def to(self) -> int | None:
        return self.recipient.profile.telegram_chat_id

    @property
    def url(self) -> str:
        return urljoin(settings.NOTICE_BASE_URL, str(self.uuid))

    @property
    def qrcode(self) -> Image:
        return qrcode.make(self.url)

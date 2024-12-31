from django.conf import settings
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='profile', on_delete=models.CASCADE
    )
    telegram_chat_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.user.username

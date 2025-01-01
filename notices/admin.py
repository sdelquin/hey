from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Notice


def url(obj) -> str:
    return mark_safe(f'<a target="blank" href="/{obj.uuid}/">/{obj.uuid}</a>')


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('pk', url, 'recipient', 'body')
    exclude = ('uuid',)

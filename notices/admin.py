import io

from django.contrib import admin
from django.http import HttpResponse
from django.utils.safestring import mark_safe

from .models import Notice


@admin.action(description='Generate QR code')
def generate_qr(modeladmin, request, queryset):  # noqa
    notice = queryset.first()
    buffer = io.BytesIO()
    notice.qrcode.save(buffer, format='PNG')
    buffer.seek(0)
    response = HttpResponse(buffer, content_type='image/png')
    return response


def url(obj) -> str:
    return mark_safe(f'<a target="blank" href="{obj.url}">{obj.url}</a>')


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('pk', url, 'recipient', 'body')
    exclude = ('uuid',)
    actions = [generate_qr]

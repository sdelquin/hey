from django.contrib import admin

from .models import Notice


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'recipient', 'body')
    exclude = ('uuid',)

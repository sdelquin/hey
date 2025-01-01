from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from telegramtk import send_message

from .models import Notice


def submit_notice(request, notice_uuid: str):
    notice = get_object_or_404(Notice, uuid=notice_uuid)
    send_message(str(notice.to), notice.body)
    return HttpResponse('Notice has been successfully sent')

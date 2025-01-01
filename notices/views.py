from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import Notice
from .tasks import send_notice


def submit_notice(request, notice_uuid: str):
    notice = get_object_or_404(Notice, uuid=notice_uuid)
    send_notice.delay(notice)
    return HttpResponse(f'{notice.recipient.first_name} será notificado/a inmediatamente!')

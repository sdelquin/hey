from django_rq import job
from telegramtk import send_message


@job
def send_notice(notice) -> None:
    send_message(notice.to, notice.body)

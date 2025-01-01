from django_rq import job
from telegramtk import send_message


@job
def send_notice(notice) -> None:
    send_message(str(notice.to), notice.body)

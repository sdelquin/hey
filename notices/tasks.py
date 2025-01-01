from django_rq import job
from telegramtk import send_message
from telegramtk.utils import escape_markdown


@job
def send_notice(notice) -> None:
    send_message(notice.to, escape_markdown(notice.body))

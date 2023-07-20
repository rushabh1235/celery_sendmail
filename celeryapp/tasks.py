from celery import shared_task
from django.core.mail import send_mail
from xyz import settings

@shared_task(bind=True)
def mail_information(self):
    mail_subject = "he! welcome to the rushabh app"
    message = "i hope you like this app and enjoy this app fetures"
    to_email = "xyz@gmail.com"
    send_mail(
        subject = mail_subject,
        message = message,
        from_email = settings.EMAIL_HOST_USER,
        recipient_list = [to_email],
        fail_silently = False,
    )
    return "Done"
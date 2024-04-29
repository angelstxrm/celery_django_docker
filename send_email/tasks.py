from settings.celery import app
from .models import Contact
from .service import send
from django.core.mail import send_mail


@app.task
def send_spam_email(user_email):
    send(user_email)


@app.task
def send_beat_email():
    for contact in Contact.objects.all():
        send_mail(
            'Вы подписались на рассылку',
            'Мы будем присылать вам много спама каждые 2 минуты',
            'danilbelenkin07@gmail.com',
            [contact.email],
            fail_silently=False,
        )

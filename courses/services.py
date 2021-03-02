from django.core.mail import send_mail

from . import models


def send(email, course_name, msg):
    send_mail(
        '#TeacHUB',
        f'{course_name} - {msg}',
        'iradmorovich@gmail.com',
        [email, ],
        fail_silently=False,
    )

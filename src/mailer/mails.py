from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse

from mailer import tokens


def send_activation_mail(user):
    token = tokens.generate_token(user)
    uid = tokens.generate_uid(user)
    mail_subject = 'Activate your account CGNetwork.'
    activation_link = f'http://localhost:8000{reverse("activate", kwargs={"uidb64": uid, "token": token})}'

    activation_message = render_to_string('activation_email.html', {
        'user': user,
        'domain': 'localhost:8000',
        'uid': uid,
        'token': token,
        'activation_link': activation_link,
    })

    send_mail(
        mail_subject,
        activation_message,
        settings.EMAIL_HOST_USER,
        [user.email],
        fail_silently=False,
    )

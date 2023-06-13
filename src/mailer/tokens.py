from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode


def generate_token(user):
    token = default_token_generator.make_token(user)
    return token


def generate_uid(user):
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    return uid
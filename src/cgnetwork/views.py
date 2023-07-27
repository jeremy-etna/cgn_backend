import datetime

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from rest_framework.views import APIView
from rest_framework.response import Response

from jwt import (
    encode
)
from cgnetwork.auth_service import authenticate_request

from cgnetwork import settings
from users.serializers import CustomUserSerializer
from users.models.common import CustomUser


@login_required()
def logged_in(request):
    role = request.user.role
    if role == "artist":
        return HttpResponseRedirect(reverse("artist-profile"))
    elif role == "company":
        return HttpResponseRedirect(reverse("company-profile"))


@login_required()
def need_delog(request):
    context = {"role": request.user.role}
    return render(request, "registration/need_delog.html", context)


def activate(request, uidb64, token):
    uid = force_str(urlsafe_base64_decode(uidb64))
    user = get_user_model().objects.get(pk=uid)
    if default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'registration/activation_confirmed.html')
    else:
        return render(request, 'registration/activation_invalid.html')


class RegisterView(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create_user(validated_data=request.data)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = CustomUser.objects.filter(email=email).first()
        if user is None:
            return Response({'error': 'User not found'}, status=400)
        if not user.check_password(password):
            return Response({'error': 'Invalid Password'}, status=400)

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow(),
        }

        token = encode(payload, settings.SECRET_KEY, algorithm='HS256')

        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response


class GetUserView(APIView):
    def get(self, request):
        user, error_response = authenticate_request(request)
        if error_response:
            return error_response

        serializer = CustomUserSerializer(user)
        return Response(serializer.data)


class LogoutView(APIView):
    def post(self, request):
        print('logout')
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'logout succeeded'
        }
        return response

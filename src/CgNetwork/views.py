from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UserRegistrationForm


def home(request):
    auth = request.user.is_authenticated
    if auth:
        user_role = request.user.user_role
        context = {}
        context['auth'] = auth
        context['user_role'] = user_role
    else:
        context = {}
        context['auth'] = auth
    return render(request, 'CgNetwork/home.html', context=context)


def register(request):
    context = {}

    auth = request.user.is_authenticated
    if auth:
        user_role = request.user.user_role
        context['auth'] = auth
        context['user_role'] = user_role
    else:
        context['auth'] = auth

    if not auth:
        if request.method == 'POST':
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                new_user = form.save(commit=False)
                new_user.save()
                return HttpResponseRedirect('../login')
            else:
                context['errors'] = form.errors

    form = UserRegistrationForm()
    context['form'] = form
    return render(request, 'registration/register.html', context=context)


@login_required()
def logged_in(request):
    user = request.user
    user_role = user.user_role
    if user_role == 'artist':
        return HttpResponseRedirect('artist/profile')
    elif user_role == 'company':
        return HttpResponseRedirect('company/profile')
    else:
        return HttpResponseRedirect('/')

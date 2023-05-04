from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from cgnetwork.forms import UserRegistrationForm


def home(request):
    auth = request.user.is_authenticated
    context = {'auth': auth}

    if auth:
        user_role = request.user.user_role
        context['user_role'] = user_role

    return render(request, 'cgnetwork/home.html', context=context)


def register(request):
    context = {}
    auth = request.user.is_authenticated

    if auth:
        role = request.user.role
        context['auth'] = auth
        context['role'] = role

    else:
        context['auth'] = auth

        if request.method == 'POST':
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                new_user = form.save(commit=False)
                new_user.save()
                return HttpResponseRedirect('../login')
            else:
                context['errors'] = form.errors
                context['form'] = form
        else:
            form = UserRegistrationForm()
            context['form'] = form

    form = UserRegistrationForm()
    context['form'] = form
    return render(request, 'registration/register.html', context=context)


@login_required()
def logged_in(request):
    role = request.user.role
    if role == 'artist':
        return HttpResponseRedirect(reverse('artist-profile'))
    elif role == 'company':
        return HttpResponseRedirect(reverse('company-profile'))


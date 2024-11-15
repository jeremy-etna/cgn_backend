from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse

from cgnetwork.forms import UserRegistrationForm


def home(request):
    auth = request.user.is_authenticated
    context = {"auth": auth}
    if auth:
        context = {"role": request.user.role}
    return render(request, "cgnetwork/home.html", context=context)


def register(request):
    context = {}
    auth = request.user.is_authenticated
    context["auth"] = auth

    if auth:
        context["role"] = request.user.role

    else:
        if request.method == "POST":
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                new_user = form.save(commit=False)
                new_user.save()
                return HttpResponseRedirect("login")
            else:
                context["errors"] = form.errors
                context["form"] = form
        else:
            form = UserRegistrationForm()
            context["form"] = form

    form = UserRegistrationForm()
    context["form"] = form
    return render(request, "registration/register.html", context=context)


def login_view(request):
    context = {}
    auth = request.user.is_authenticated
    context["auth"] = auth

    if auth:
        context["role"] = request.user.role
        return HttpResponseRedirect(reverse("need_delog"))

    else:
        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password"]
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect("logged_in")
                else:
                    form.add_error(None, "Invalid username or password")
        else:
            form = AuthenticationForm()

    context["form"] = form
    return render(request, "registration/login.html", context)


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


def logout_view(request):
    logout(request)
    return redirect("login")

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.datetime_safe import datetime
from .forms import *
from .models import Job
from artist.models import Artist

from .data_manager import (
    get_profile_data,
    get_artist_data,
    get_job_data,
    )


@login_required()
def profile(request):
    user = request.user
    user_role = user.user_role
    context = get_profile_data(user)
    context['user_role'] = user_role
    return render(request, 'company/profile.html', context=context)


@login_required()
def profile_edit(request):
    user = request.user
    user_role = request.user.user_role
    context = {}
    context['user_role'] = user_role
    if request.method == 'POST':
        def submit_form(Form, instance):
            form = Form(request.POST, request.FILES, instance=instance)
            if form.is_valid():
                form.save()
            else:
                context['errors'] = form.errors
        submit_form(CompanyIdentityForm, user.company)
        submit_form(CompanyCoordonatesForm, user)
        submit_form(CompanyUrlForm, user.company)
        submit_form(CompanySectorForm, user.company)
        return HttpResponseRedirect('../')
    else:
        context = get_profile_data(user)
        context['user_role'] = user_role
        context['CompanyIdentityForm'] = CompanyIdentityForm(initial=context['identity'])
        context['CompanyCoordonatesForm'] = CompanyCoordonatesForm(initial=context['coordonates'])
        context['CompanySectorForm'] = CompanySectorForm(initial=context['sectors'])
        context['CompanyUrlForm'] = CompanyUrlForm(initial=context['urls'])
    return render(request, 'company/profile_edit.html', context=context)


@login_required()
def artists(request):
    user = request.user
    user_role = user.user_role
    context = {}
    context['user_role'] = user_role
    context['artists'] = Artist.objects.all()
    return render(request, 'company/artists.html', context=context)


@login_required()
def artist(request, id):
    user = request.user
    user_role = user.user_role
    artist = Artist.objects.get(id=id)
    context = get_artist_data(artist)
    context['user_role'] = user_role
    return render(request, 'company/artist.html', context=context)


@login_required()
def job_create(request):
    user = request.user
    user_role = user.user_role
    context = {}
    context['user_role'] = user_role
    if request.method == 'POST':
        entry = Job.objects.create(
            user=user,
            company_size=user.company.company_size,
            company_name=user.company.company_name,
            creation_date=datetime.now(),
            logo=user.company.logo
        )
        entry.save()

        def submit_form(Form):
            form = Form(request.POST, request.FILES, instance=entry)
            if form.is_valid():
                form.save()
            else:
                context['errors'] = form.errors
                entry.delete()

        submit_form(JobForm)
        submit_form(JobArtisticSkillForm)
        submit_form(JobSoftwareForm)
        return HttpResponseRedirect('../')
    else:
        context['JobForm'] = JobForm()
        context['JobArtisticSkillForm'] = JobArtisticSkillForm()
        context['JobSoftwareForm'] = JobSoftwareForm()
    return render(request, 'company/job_create.html', context=context)


@login_required()
def job(request, id):
    user = request.user
    user_role = user.user_role
    job = Job.objects.get(id=id)
    context = get_job_data(job)
    context['user_role'] = user_role
    return render(request, 'company/job.html', context=context)


@login_required()
def jobs(request):
    user = request.user
    user_role = user.user_role
    context = {}
    context['user_role'] = user_role
    jobs = Job.objects.filter(user=user)
    context['jobs'] = jobs
    return render(request, 'company/jobs.html', context=context)


@login_required()
def job_delete(request, id):
    user = request.user
    user_role = user.user_role
    context = {}
    context['user_role'] = user_role
    Job.objects.get(id=id).delete()
    return HttpResponseRedirect('../')

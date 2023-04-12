from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.datetime_safe import datetime

from users.forms.company import *
from job.models import Job
from users.models.artist import Artist

from users.data_managers.company import (
    get_profile_data,
    convert_objects_to_dict,
)


@login_required()
def profile(request):
    user_id = request.user.id
    context = get_profile_data(user_id)
    context = convert_objects_to_dict(context)
    context['user_role'] = request.user.user_role
    return render(request, 'company/profile.html', context)


@login_required()
def profile_edit(request):
    user_id = request.user.id
    context = get_profile_data(user_id)
    context['user_role'] = request.user.user_role

    forms_and_instances = [
        (CompanyIdentityForm, context['identity']),
        (CompanyCoordinateForm, context['coordinate']),
        (CompanyCompetenceForm, context['competence']),
        (CompanySectorForm, context['sector']),
        (CompanySocialMediaForm, context['socialMedia']),
        (CompanySoftwareForm, context['software']),
    ]

    if request.method == 'POST':
        for form, instance in forms_and_instances:
            current_form = form(request.POST, request.FILES, instance=instance)
            if current_form.is_valid():
                current_form.save()
            else:
                context['errors'] = current_form.errors
        return HttpResponseRedirect('../')
    else:
        for form, instance in forms_and_instances:
            context[form.__name__] = form(initial=instance)

    return render(request, 'company/profile_edit.html', context)


@login_required()
def artists(request):
    user_role = request.user.user_role
    context = {}
    context['user_role'] = user_role
    context['artists'] = Artist.objects.all()
    return render(request, 'company/artists.html', context=context)


@login_required()
def artist(request, id):
    user_role = request.user.user_role
    artist = Artist.objects.get(id=id)
    context = get_artist_data(artist)
    context['user_role'] = user_role
    return render(request, 'company/artist.html', context=context)


@login_required()
def job_create(request):
    user_role = request.user.user_role
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
    user_role = request.user.user_role
    job = Job.objects.get(id=id)
    context = get_job_data(job)
    context['user_role'] = user_role
    return render(request, 'company/job.html', context=context)


@login_required()
def jobs(request):
    user_role = request.user.user_role
    context = {}
    context['user_role'] = user_role
    jobs = Job.objects.filter(user=user)
    context['jobs'] = jobs
    return render(request, 'company/jobs.html', context=context)


@login_required()
def job_delete(request, id):
    user_role = request.user.user_role
    context = {}
    context['user_role'] = user_role
    Job.objects.get(id=id).delete()
    return HttpResponseRedirect('../')

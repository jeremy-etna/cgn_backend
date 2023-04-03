from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import *
from company.models import Job
from company.models import Company

from .data_manager import (
    get_profile_data,
    get_job_data,
    get_company_data,
    )


@login_required()
def profile(request):
    user = request.user
    user_role = user.user_role
    context = get_profile_data(user)
    context['user_role'] = user_role
    return render(request, 'artist/profile.html', context=context)


@login_required()
def profile_edit(request):
    user = request.user
    user_role = user.user_role
    context = {}
    context['user_role'] = user_role

    if request.method == 'POST':
        def submit_form(Form, instance):
            form = Form(request.POST, request.FILES, instance=instance)
            if form.is_valid():
                form.save()
            else:
                context['errors'] = form.errors

        submit_form(ArtistIdentityForm, user.artist)
        submit_form(ArtistCoordonatesForm, user)
        submit_form(ArtistSectorForm, user.artist)
        submit_form(ArtistContractForm, user.artist)
        submit_form(ArtistUrlForm, user.artist)
        submit_form(ArtistArtisticSkillForm, user.artist)
        submit_form(ArtistSoftwareForm, user.artist)
        return HttpResponseRedirect('../')
    else:
        context = get_profile_data(user)
        context['user_role'] = user_role
        context['ArtistIdentityForm'] = ArtistIdentityForm(initial=context['identity'])
        context['ArtistCoordonatesForm'] = ArtistCoordonatesForm(initial=context['coordonates'])
        context['ArtistContractForm'] = ArtistContractForm(initial=context['contracts'])
        context['ArtistArtisticSkillForm'] = ArtistArtisticSkillForm(initial=context['artistic_skills'])
        context['ArtistSectorForm'] = ArtistSectorForm(initial=context['sectors'])
        context['ArtistUrlForm'] = ArtistUrlForm(initial=context['urls'])
        context['ArtistSoftwareForm'] = ArtistSoftwareForm(initial=context['softwares'])
    return render(request, 'artist/profile_edit.html', context=context)


@login_required()
def jobs(request):
    user = request.user
    user_role = user.user_role
    context = {}

    jobs = Job.objects.all()
    paginator = Paginator(jobs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context['user_role'] = user_role
    context['jobs'] = page_obj
    return render(request, 'artist/jobs.html', context=context)


@login_required()
def job(request, id):
    user = request.user
    user_role = user.user_role
    job = Job.objects.get(id=id)
    context = get_job_data(job)
    context['user_role'] = user_role

    return render(request, 'artist/job.html', context=context)


@login_required()
def companies(request):
    user = request.user
    user_role = user.user_role
    companies = Company.objects.all()
    context = {}
    context['user_role'] = user_role
    context['companies'] = companies
    return render(request, 'artist/companies.html', context=context)


@login_required()
def company(request, id):
    user = request.user
    user_role = user.user_role
    company = Company.objects.get(id=id)
    context = get_company_data(company)
    context['user_role'] = user_role

    return render(request, 'artist/company.html', context=context)

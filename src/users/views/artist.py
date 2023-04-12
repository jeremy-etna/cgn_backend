from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render

from users.forms.artist import *
from job.models import Job
from users.models.company import Company


from users.data_managers.artist import (
    get_profile_data,
    convert_objects_to_dict,
    get_job_data,
    get_company_data,
)


@login_required()
def profile(request):
    user_id = request.user.id
    context = get_profile_data(user_id)
    context = convert_objects_to_dict(context)
    context['user_role'] = request.user.user_role
    return render(request, 'artist/profile.html', context)


@login_required()
def profile_edit(request):
    user_id = request.user.id
    context = get_profile_data(user_id)
    context['user_role'] = request.user.user_role

    forms_and_instances = [
        (ArtistIdentityForm, context['identity']),
        (ArtistCoordinateForm, context['coordinate']),
        (ArtistContractForm, context['contract']),
        (ArtistCompetenceForm, context['competence']),
        (ArtistSectorForm, context['sector']),
        (ArtistSocialMediaForm, context['socialMedia']),
        (ArtistSoftwareForm, context['software']),
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
        for form_class, instance in forms_and_instances:
            form = form_class(instance=instance)
            context[form_class.__name__] = form

    return render(request, 'artist/profile_edit.html', context)


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

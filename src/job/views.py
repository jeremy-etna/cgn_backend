import os
from django.contrib.auth.decorators import login_required
from django.http import (
    HttpResponseRedirect,
)
from django.utils.datetime_safe import datetime
from django.utils.html import escape

from django.shortcuts import render
from django.forms.models import model_to_dict
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from job.models import Job
from job.forms import JobCreationForm

from users.services.models_selector import (
    CONTEXT_TEMPLATE,
    COMPANY_PROFILE_MODELS,
)


@login_required()
def jobs(request):
    jobs = Job.objects.all()
    if request.user.role == 'company':
        jobs = Job.objects.filter(user_id=request.user.id)
    paginator = Paginator(jobs, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = CONTEXT_TEMPLATE
    context['role'] = request.user.role
    context['objects'] = page_obj
    context["paginator_template_path"] = os.path.join("common", "components", "paginator.html")
    return render(request, 'jobs.html', context)


@login_required()
def job(request, id):
    context = CONTEXT_TEMPLATE.copy()
    context['role'] = request.user.role
    context['objects'] = {
        'job': None,
        'company': None,
    }
    current_job = Job.objects.get(id=id)
    company_identity = COMPANY_PROFILE_MODELS[0]
    company_data = company_identity.objects.get(user_id=current_job.user_id)
    context['objects']['job'] = model_to_dict(current_job, exclude=['user', 'id'])
    context['objects']['company'] = model_to_dict(company_data, exclude=['user', 'id'])
    return render(request, 'job.html', context)


@login_required()
def job_creation(request):
    if request.user.role != 'company':
        return render(request, 'cgnetwork/404.html', status=404)

    model_fields = ['title', 'company_description', 'job_responsibilities', 'required_skills',
                    'required_qualifications', 'job_requirements', 'employee_benefits', 'salary_min', 'salary_max']
    user = request.user
    context = CONTEXT_TEMPLATE

    if request.method == 'POST':
        form = JobCreationForm(request.POST)
        if form.is_valid():
            new_job = form.save(commit=False)
            new_job.user = user
            new_job.creation_date = datetime.now()
            for field in model_fields:
                setattr(new_job, field, escape(getattr(new_job, field)))
            new_job.save()
            return HttpResponseRedirect(f'../job/{new_job.id}')
        else:
            context['errors'] = form.errors
    else:
        context['form'] = JobCreationForm()

    return render(request, 'job_create.html', context)





from django.contrib.auth.decorators import login_required
from django.http import (
    HttpResponseRedirect,
    HttpResponseForbidden,
)
from django.utils.datetime_safe import datetime
from django.utils.html import escape

from django.shortcuts import render
from django.forms.models import model_to_dict
from django.core.paginator import Paginator

from job.models import Job
from job.forms import JobCreationForm

from job.data_manager import (
    get_profile_data,
)


@login_required()
def jobs(request):
    user_id = request.user.id

    jobs = Job.objects.all()

    paginator = Paginator(jobs, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {}
    context['user_role'] = request.user.user_role
    context['jobs'] = page_obj
    # context['jobs'] = jobs

    return render(request, 'jobs.html', context)


@login_required()
def job(request, id):
    context = {}
    user = request.user
    context['user_role'] = user.user_role
    current_job = Job.objects.get(id=id)
    context['job'] = model_to_dict(current_job, exclude=['user', 'id'])
    context['user'] = {
        'company_name': user.company.company_name,
        'description': user.company.description,
        'company_size': user.company.company_size,
    }
    print(context['user'])
    return render(request, 'job.html', context)


@login_required()
def job_creation(request):
    if request.user.user_role != 'company':
        return render(request, 'cgnetwork/404.html', status=404)

    model_fields = ['title', 'company_description', 'job_responsibilities', 'required_skills',
                    'required_qualifications', 'job_requirements', 'employee_benefits', 'salary_min', 'salary_max']
    user = request.user
    context = {}

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





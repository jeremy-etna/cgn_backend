import os

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.forms.models import model_to_dict
from django.http import (
    HttpResponseRedirect,
)
from django.shortcuts import render
from django.utils.datetime_safe import datetime
from django.utils.html import escape
from rest_framework.response import Response
from rest_framework.views import APIView

from cgnetwork.auth_service import authenticate_request
from job.forms import JobCreationForm
from job.serializers import JobSerializer
from users.serializers import CustomUserSerializer
from users.services.models_selector import (
    COMPANY_PROFILE_MODELS,
)
from users.services.objects_manager import (
    get_template,
)

from .models import Job
from rest_framework.pagination import PageNumberPagination
from rest_framework import (
    generics,
    exceptions
)



# @login_required()
# def jobs(request):
#     jobs = Job.objects.all()
#
#     if request.user.role == 'company':
#         jobs = Job.objects.filter(user_id=request.user.id)
#
#     paginator = Paginator(jobs, 5)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#
#     context = {"role": request.user.role, "objects": page_obj, "templates_models": {}, "templates_ui": {}}
#
#     context["templates_ui"]["card"] = os.path.join(
#         "components", "job_card.html"
#     )
#     context["templates_ui"]["paginator"] = get_template(
#         "cgnetwork", "cgnetwork", "paginator.html"
#     )
#     return render(request, 'jobs.html', context)
#
#
# @login_required()
# def job(request, id):
#     context = {"role": request.user.role, "objects": {}, "templates_models": {}, "templates_ui": {}, 'objects': {
#         'job': None,
#         'company': None,
#     }}
#     current_job = Job.objects.get(id=id)
#
#     company_identity = COMPANY_PROFILE_MODELS[0]
#     company_identity_data = company_identity.objects.get(user_id=current_job.user_id)
#
#     company_coordinate = COMPANY_PROFILE_MODELS[1]
#     company_coordinate_data = company_coordinate.objects.get(user_id=current_job.user_id)
#
#     context['objects']['job'] = model_to_dict(current_job, exclude=['user', 'id'])
#     context['objects']['identity'] = model_to_dict(company_identity_data, exclude=['user', 'id'])
#     context['objects']['coordinate'] = model_to_dict(company_coordinate_data, exclude=['user', 'id'])
#     return render(request, 'job.html', context)
#
#
# @login_required()
# def job_create(request):
#     if request.user.role != 'company':
#         return render(request, 'cgnetwork/404.html', status=404)
#
#     model_fields = ['title', 'company_description', 'job_responsibilities', 'required_skills',
#                     'required_qualifications', 'job_requirements', 'employee_benefits', 'salary_min', 'salary_max']
#     user = request.user
#     context = {"role": request.user.role, "objects": {}, "templates_models": {}, "templates_ui": {}}
#
#     if request.method == 'POST':
#         form = JobCreationForm(request.POST)
#         if form.is_valid():
#             new_job = form.save(commit=False)
#             new_job.user = user
#             new_job.creation_date = datetime.now()
#             company = COMPANY_PROFILE_MODELS[0].objects.get(user_id=user.id)
#             new_job.company = company
#             for field in model_fields:
#                 setattr(new_job, field, escape(getattr(new_job, field)))
#             new_job.save()
#             return HttpResponseRedirect(f'../{new_job.id}')
#         else:
#             context['errors'] = form.errors
#             print(context['errors'])
#     else:
#         context['form'] = JobCreationForm()
#
#     return render(request, 'job_create.html', context)
#
#
# @login_required()
# def job_delete(request, job_id):
#     if request.user.role != 'company':
#         return render(request, 'cgnetwork/404.html', status=404)
#
#     context = {"role": request.user.role, "objects": {}, "templates_models": {}, "templates_ui": {}}
#
#     Job.objects.get(id=job_id).delete()
#     return HttpResponseRedirect('../../all')



class JobListView(generics.ListAPIView):
    serializer_class = JobSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        user, error_response = authenticate_request(self.request)
        if error_response:
            raise exceptions.NotAuthenticated()
        if user.role == 'company':
            return Job.objects.filter(user_id=user.id)
        else:
            return Job.objects.all()


class JobView(generics.RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    lookup_field = 'id'

    def get_object(self):
        user, error_response = authenticate_request(self.request)
        if error_response:
            raise exceptions.NotAuthenticated()
        return super().get_object()


class JobCreateView(generics.CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def create(self, request, *args, **kwargs):
        user, error_response = authenticate_request(request)
        if error_response:
            raise exceptions.NotAuthenticated()

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

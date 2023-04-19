import os
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

from users.forms.artist import *
from users.models.company import Company

from users.data_managers.artist import (
    get_profile_data,
    convert_objects_to_dict,
    get_templates,
)

COMPONENTS = [
    'identity',
    'coordinate',
    'administrative',
    'contract',
    'competence',
    'mobility',
    'sector',
    'socialMedia',
    'software',
]


@login_required()
def profile(request):
    user_id = request.user.id
    context = get_profile_data(user_id)
    context = convert_objects_to_dict(context)
    context['user_role'] = request.user.user_role
    context['templates'] = get_templates(context['user_role'], COMPONENTS)
    return render(request, os.path.join('artist', 'profile.html'), context)


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
        (ArtistAdministrativeForm, context['administrative']),
        (ArtistMobilityForm, context['mobility']),
        (ArtistSectorForm, context['sector']),
        (ArtistSocialMediaForm, context['socialMedia']),
        (ArtistSoftwareForm, context['software']),
    ]

    # Vérifier que toutes les instances appartiennent à l'utilisateur connecté
    for _, instance in forms_and_instances:
        if instance.user_id != user_id:
            return HttpResponseForbidden("Accès non autorisé")

    if request.method == 'POST':
        for form, instance in forms_and_instances:
            current_form = form(request.POST, request.FILES, instance=instance)
            form_name = request.POST.get('current-form', '')
            if current_form.is_valid() and form_name == form.__name__:
                current_form.save()
                break
            else:
                context['errors'] = current_form.errors
            return HttpResponseRedirect('../')
    else:
        context['forms'] = {}
        for form_class, instance in forms_and_instances:
            form = form_class(instance=instance)
            context['forms'][form_class.__name__] = form
            context['templates'] = get_templates(context['user_role'], ['form_edit_template'])

    return render(request, os.path.join('artist', 'profile_edit.html'), context)


@login_required()
def artists(request):
    user_role = request.user.user_role
    context = {
        'user_role': user_role,
        'users': Artist.objects.all(),
        'card_template_path': os.path.join('artist', 'components', 'artist_card.html'),
    }
    return render(request, os.path.join('artist', 'gallery.html'), context)


@login_required()
def companies(request):
    user_role = request.user.user_role
    context = {
        'user_role': user_role,
        'users': Company.objects.all(),
        'card_template_path': os.path.join('artist', 'components', 'company_card.html'),
    }
    return render(request, os.path.join('artist', 'gallery.html'), context)





@login_required()
def company(request, id):
    user = request.user
    context = {
        'user_role': user.user_role,
        'company': Company.objects.get(id=id)
    }
    return render(request, os.path.join('artist', 'gallery.html'), context)

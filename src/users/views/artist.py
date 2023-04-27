import os

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

from users.data_manager import (
    get_artist_profile_data,
    convert_objects_to_dict,
    get_templates,
    # get_artist_card_data,
)
from users.forms.artist import *

from users.models.artist import Artist
from users.models.company import Company

from cgnetwork.context import TemplateResolver, ContextBuilder, FormResolver, ObjectResolver
from cgnetwork.constants import ARTIST_COMPONENTS



@login_required()
def profile(request):
    # user_id = request.user.id
    # context ={}
    # context["objects"] = {}
    # objects = get_artist_profile_data(user_id)
    # context["objects"] = convert_objects_to_dict(objects)
    # context["user_role"] = request.user.user_role
    # context["templates"] = {}
    # context["templates"]["models"] = {}
    # context["templates"]["ui"] = {}
    # context["templates"]["models"]["identity"] = os.path.join('artist', 'components', 'artist.html')
    # context["templates"]["models"]["coordinate"] = os.path.join('common', 'components', 'coordinate.html')
    # context["templates"]["models"]["administrative"] = os.path.join('artist', 'components', 'administrative.html')
    # context["templates"]["models"]["mobility"] = os.path.join('common', 'components', 'mobility.html')
    # context["templates"]["models"]["socialMedia"] = os.path.join('common', 'components', 'socialMedia.html')
    # context["templates"]["models"]["contract"] = os.path.join('artist', 'components', 'contract.html')
    # context["templates"]["models"]["sector"] = os.path.join('common', 'components', 'sector.html')
    # context["templates"]["models"]["competence"] = os.path.join('artist', 'components', 'competence.html')
    # context["templates"]["models"]["software"] = os.path.join('common', 'components', 'software.html')
    # context["templates"]["ui"]["navbar_vertical"] = os.path.join('common', 'components', 'navbar_vertical.html')

    context = {}
    context["templates"] = {}
    resolved_templates = TemplateResolver(request.user.user_role)
    models_templates = resolved_templates.get_templates('users', ARTIST_COMPONENTS, 'models')
    ui_templates = resolved_templates.get_templates('users', ['navbar_vertical'], 'ui')
    context["templates"]["models"] = models_templates
    # context["templates"]["ui"] = ui_templates

    context["objects"] = {}
    objects = get_artist_profile_data(request.user.id)
    context["objects"] = convert_objects_to_dict(objects)

    # form_resolver = FormResolver(request.user.user_role, 'users')
    # resolved_forms = form_resolver.get_forms(ARTIST_COMPONENTS)
    # print(resolved_forms)

    object_resolver = ObjectResolver(request.user.user_role, request.user.id)
    objects = object_resolver.get_objects_by_name(['cgnetwork', 'users'], ARTIST_COMPONENTS)
    print(objects)


    return render(request, os.path.join("artist", "profile.html"), context)

@login_required()
def profile_edit(request):
    COMPONENTS = [
        'form_edit',
        'navbar_vertical'
    ]
    user_id = request.user.id
    context = get_artist_profile_data(user_id)
    context["user_role"] = request.user.user_role

    forms_and_instances = [
        (ArtistArtistForm, context["identity"]),
        (ArtistCoordinateForm, context["coordinate"]),
        (ArtistAdministrativeForm, context["administrative"]),
        (ArtistMobilityForm, context["mobility"]),
        (ArtistSocialMediaForm, context["socialMedia"]),
        (ArtistContractForm, context["contract"]),
        (ArtistSectorForm, context["sector"]),
        (ArtistCompetenceForm, context["competence"]),
        (ArtistSoftwareForm, context["software"]),
    ]

    # Vérifier que toutes les instances appartiennent à l'utilisateur connecté
    for _, instance in forms_and_instances:
        if instance.user_id != user_id:
            return HttpResponseForbidden("Accès non autorisé")

    if request.method == "POST":
        form_saved = False
        for form, instance in forms_and_instances:
            current_form = form(request.POST, request.FILES, instance=instance)
            form_name = request.POST.get("current-form", "")
            if form_name == form.__name__:
                if current_form.is_valid():
                    current_form.save()
                    form_saved = True
                    break
                else:
                    context["errors"] = current_form.errors
        if form_saved:
            return HttpResponseRedirect("../")
    else:
        context["forms"] = {}
        for form_class, instance in forms_and_instances:
            form = form_class(instance=instance)
            context["forms"][form_class.__name__] = form
            context["templates"] = get_templates('common', COMPONENTS)
    return render(request, os.path.join("artist", "profile_edit.html"), context)


@login_required()
def artists(request):
    user_role = request.user.user_role
    artists_list = Artist.objects.all()

    paginator = Paginator(artists_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "user_role": user_role,
        "objects": page_obj,
        "card_template_path": os.path.join("artist", "components", "artist_card.html"),
        "paginator_template_path": os.path.join(
            "common", "components", "paginator.html"
        ),
    }
    return render(request, os.path.join("common", "gallery.html"), context)


@login_required()
def companies(request):
    user_role = request.user.user_role
    companies = Company.objects.all()

    paginator = Paginator(companies, 25)
    page = request.GET.get("page")

    try:
        companies = paginator.page(page)
    except PageNotAnInteger:
        companies = paginator.page(1)
    except EmptyPage:
        companies = paginator.page(paginator.num_pages)

    context = {
        "user_role": user_role,
        "users": companies,
        "card_template_path": os.path.join("artist", "components", "company_card.html"),
        "paginator_template_path": os.path.join(
            "common", "components", "paginator.html"
        ),
    }
    return render(request, os.path.join("common", "gallery.html"), context)


@login_required()
def company(request, id):
    user = request.user
    context = {"user_role": user.user_role, "company": Company.objects.get(id=id)}
    return render(request, os.path.join("artist", "gallery.html"), context)

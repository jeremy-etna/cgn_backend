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
from users.models.company import Company

COMPONENTS = [
    "identity",
    "coordinate",
    "administrative",
    "mobility",
    "socialMedia",
    "contract",
    "sector",
    "competence",
    "software",
]


@login_required()
def profile(request):
    user_id = request.user.id
    context = get_artist_profile_data(user_id)
    context = convert_objects_to_dict(context)
    context["user_role"] = request.user.user_role
    context["templates"] = {}
    context["templates"]["identity"] = os.path.join('artist', 'components', 'identity.html')
    context["templates"]["coordinate"] = os.path.join('common', 'components', 'coordinate.html')
    context["templates"]["administrative"] = os.path.join('artist', 'components', 'administrative.html')
    context["templates"]["mobility"] = os.path.join('common', 'components', 'mobility.html')
    context["templates"]["socialMedia"] = os.path.join('common', 'components', 'socialMedia.html')
    context["templates"]["contract"] = os.path.join('artist', 'components', 'contract.html')
    context["templates"]["sector"] = os.path.join('common', 'components', 'sector.html')
    context["templates"]["competence"] = os.path.join('artist', 'components', 'competence.html')
    context["templates"]["software"] = os.path.join('common', 'components', 'software.html')
    context["navbar_vertical"] = os.path.join('common', 'components', 'navbar_vertical.html')
    print(context)
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
        (ArtistIdentityForm, context["identity"]),
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

import os
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.conf import settings

from users.services.objects_manager import (
    get_objects_from_models,
    remove_elements_by_keys_recursive,
    remove_pattern_dict_keys,
    get_templates,
    get_template,
)

from users.services.models_selector import (
    ARTIST_PROFILE_MODELS,
    ARTIST_PROFILE_FORMS,
    COMPANY_PROFILE_MODELS,
)


@login_required()
def profile(request):
    objects = get_objects_from_models(ARTIST_PROFILE_MODELS, request.user.id)
    objects = remove_elements_by_keys_recursive(objects, ["id", "user", "user_id"])
    objects = remove_pattern_dict_keys(objects, "artist")
    context = {"role": request.user.role, "objects": objects, "templates_models": {}, "templates_ui": {}}

    context["templates_models"]["identity"] = os.path.join(
        "artist", "components", "identity.html"
    )
    context["templates_models"]["coordinate"] = os.path.join(
        "common", "components", "coordinate.html"
    )
    context["templates_models"]["administrative"] = os.path.join(
        "artist", "components", "administrative.html"
    )
    context["templates_models"]["mobility"] = os.path.join(
        "common", "components", "mobility.html"
    )
    context["templates_models"]["socialMedia"] = os.path.join(
        "common", "components", "socialMedia.html"
    )
    context["templates_models"]["contract"] = os.path.join(
        "artist", "components", "contract.html"
    )
    context["templates_models"]["sector"] = os.path.join(
        "common", "components", "sector.html"
    )
    context["templates_models"]["competence"] = os.path.join(
        "artist", "components", "competence.html"
    )
    context["templates_models"]["software"] = os.path.join(
        "artist", "components", "software.html"
    )
    context["templates_ui"]["navbar_vertical"] = os.path.join(
        "common", "components", "navbar_vertical.html"
    )
    return render(request, os.path.join("artist", "profile.html"), context)


class ProfileEditView(LoginRequiredMixin, View):
    COMPONENTS = ["form_edit", "navbar_vertical"]
    context_keys = [
        str(form.__name__).replace("Form", "").lower() for form in ARTIST_PROFILE_FORMS
    ]
    forms_and_instances = list(zip(context_keys, ARTIST_PROFILE_FORMS))

    def get(self, request):
        context = {
            "role": request.user.role,
            "objects": {},
            "templates_models": {},
            "templates_ui": {},
            "forms": {},
        }

        model_instances = {}

        for model_name in self.context_keys:
            model_instances[model_name] = getattr(request.user, model_name)

        for instance_name, form_class in self.forms_and_instances:
            instance = model_instances[instance_name]
            form = form_class(instance=instance)
            context["forms"][form_class.__name__] = form

        context["templates"] = get_templates("common", self.COMPONENTS)
        return render(request, os.path.join("artist", "profile_edit.html"), context)

    def post(self, request):
        context = {
            "role": request.user.role,
            "objects": {},
            "templates_models": {},
            "templates_ui": {},
        }

        form_saved = False
        model_instances = {}
        for model_name in self.context_keys:
            model_instances[model_name] = getattr(request.user, model_name)
        for instance_name, form_class in self.forms_and_instances:
            instance = model_instances[instance_name]
            current_form = form_class(request.POST, request.FILES, instance=instance)
            form_name = request.POST.get("current-form", "")
            if form_name == form_class.__name__:
                if current_form.is_valid():
                    current_form.save()
                    form_saved = True
                    break
                else:
                    context["errors"] = current_form.errors

        if form_saved:
            return HttpResponseRedirect(
                "../"
                + "#"
                + form_name.lower().replace("form", "").replace("artist", "")
                + "-section"
            )
        else:
            context["templates"] = get_templates("common", self.COMPONENTS)
            return render(request, os.path.join("artist", "profile_edit.html"), context)


@login_required()
def artists(request):
    artist_identity = ARTIST_PROFILE_MODELS[0]
    artists_list = artist_identity.objects.all().order_by("id")

    paginator = Paginator(artists_list, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "role": request.user.role,
        "objects": page_obj,
        "templates_models": {},
        "templates_ui": {},
    }

    context["templates_ui"]["card"] = os.path.join(
        "artist", "components", "artist_card.html"
    )
    context["templates_ui"]["paginator"] = get_template(
        "cgnetwork", "cgnetwork", "paginator.html"
    )
    return render(request, os.path.join("common", "gallery.html"), context)


@login_required()
def companies(request):
    company_identity = COMPANY_PROFILE_MODELS[0]
    companies_list = company_identity.objects.all().order_by("id")

    paginator = Paginator(companies_list, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "role": request.user.role,
        "objects": page_obj,
        "templates_models": {},
        "templates_ui": {},
    }

    context["templates_ui"]["card"] = os.path.join(
        "company", "components", "company_card.html"
    )
    context["templates_ui"]["paginator"] = get_template(
        "cgnetwork", "cgnetwork", "paginator.html"
    )
    return render(request, os.path.join("common", "gallery.html"), context)


@login_required()
def artist(request, id):
    objects = get_objects_from_models(ARTIST_PROFILE_MODELS, id)
    objects = remove_elements_by_keys_recursive(objects, ["id", "user", "user_id"])
    objects = remove_pattern_dict_keys(objects, "artist")
    context = {
        "role": request.user.role,
        "objects": objects,
        "templates_models": {},
        "templates_ui": {},
    }

    context["templates_models"]["identity"] = os.path.join(
        "artist", "components", "identity.html"
    )
    context["templates_models"]["coordinate"] = os.path.join(
        "common", "components", "coordinate.html"
    )
    context["templates_models"]["administrative"] = os.path.join(
        "artist", "components", "administrative.html"
    )
    context["templates_models"]["mobility"] = os.path.join(
        "common", "components", "mobility.html"
    )
    context["templates_models"]["socialMedia"] = os.path.join(
        "common", "components", "socialMedia.html"
    )
    context["templates_models"]["contract"] = os.path.join(
        "artist", "components", "contract.html"
    )
    context["templates_models"]["sector"] = os.path.join(
        "common", "components", "sector.html"
    )
    context["templates_models"]["competence"] = os.path.join(
        "artist", "components", "competence.html"
    )
    context["templates_models"]["software"] = os.path.join(
        "artist", "components", "software.html"
    )
    context["templates_ui"]["navbar_vertical"] = os.path.join(
        "common", "components", "navbar_vertical.html"
    )
    return render(
        request,
        os.path.join(
            settings.BASE_DIR, "users", "templates", "artist", "profile_public.html"
        ),
        context,
    )


@login_required()
def company(request, id):
    objects = get_objects_from_models(COMPANY_PROFILE_MODELS, id)
    objects = remove_elements_by_keys_recursive(objects, ["id", "user", "user_id"])
    objects = remove_pattern_dict_keys(objects, "company")
    context = {
        "role": request.user.role,
        "objects": objects,
        "templates_models": {},
        "templates_ui": {},
    }

    context["templates_models"]["identity"] = os.path.join(
        "company", "components", "identity.html"
    )
    context["templates_models"]["coordinate"] = os.path.join(
        "common", "components", "coordinate.html"
    )
    context["templates_models"]["mobility"] = os.path.join(
        "common", "components", "mobility.html"
    )
    context["templates_models"]["socialMedia"] = os.path.join(
        "common", "components", "socialMedia.html"
    )
    context["templates_models"]["sector"] = os.path.join(
        "common", "components", "sector.html"
    )
    context["templates_models"]["competence"] = os.path.join(
        "company", "components", "competence.html"
    )
    context["templates_models"]["software"] = os.path.join(
        "company", "components", "software.html"
    )
    context["templates_ui"]["navbar_vertical"] = os.path.join(
        "common", "components", "navbar_vertical.html"
    )
    return render(
        request,
        os.path.join(
            settings.BASE_DIR, "users", "templates", "company", "profile_public.html"
        ),
        context,
    )

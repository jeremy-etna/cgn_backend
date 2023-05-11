import os

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from users.services.objects_manager import (
    get_objects_from_models,
    remove_elements_by_keys_recursive,
    remove_pattern_dict_keys,
    get_templates,
)

from users.services.models_selector import (
    CONTEXT_TEMPLATE,
    ARTIST_PROFILE_MODELS,
    COMPANY_PROFILE_MODELS,
    COMPANY_PROFILE_FORMS,
)


@login_required()
def profile(request):
    objects = get_objects_from_models(COMPANY_PROFILE_MODELS, request.user.id)
    objects = remove_elements_by_keys_recursive(objects, ["id", "user", "user_id"])
    objects = remove_pattern_dict_keys(objects, "company")
    context = CONTEXT_TEMPLATE
    context["role"] = request.user.role
    context["objects"] = objects
    context["templates_models"]["company"] = os.path.join(
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
    return render(request, os.path.join("company", "profile.html"), context)


class ProfileEditView(View):
    COMPONENTS = ["form_edit", "navbar_vertical"]
    context_keys = [
        str(form.__name__).replace("Form", "").lower() for form in COMPANY_PROFILE_FORMS
    ]
    forms_and_instances = list(zip(context_keys, COMPANY_PROFILE_FORMS))

    def get(self, request):
        context = CONTEXT_TEMPLATE
        context["role"] = request.user.role
        model_instances = {}
        for model_name in self.context_keys:
            model_instances[model_name] = getattr(request.user, model_name)
        for instance_name, form_class in self.forms_and_instances:
            instance = model_instances[instance_name]
            form = form_class(instance=instance)
            context["forms"][form_class.__name__] = form

        context["templates"] = get_templates("common", self.COMPONENTS)
        return render(request, os.path.join("company", "profile_edit.html"), context)

    def post(self, request):
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
                    self.context["errors"] = current_form.errors

        if form_saved:
            return HttpResponseRedirect(
                "../"
                + "#"
                + form_name.replace("Form", "").replace("Company", "").lower()
            )
        else:
            return render(request, "profile_edit.html", self.context)


@login_required()
def artists(request):
    artist_identity = ARTIST_PROFILE_MODELS[0]
    artists_list = artist_identity.objects.all().order_by("id")

    paginator = Paginator(artists_list, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = CONTEXT_TEMPLATE
    context["objects"] = page_obj
    context["role"] = request.user.role
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

    paginator = Paginator(companies_list, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = CONTEXT_TEMPLATE
    context["objects"] = page_obj
    context["role"] = request.user.role
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
    context = CONTEXT_TEMPLATE
    context["role"] = request.user.role
    context["objects"] = objects
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
    return render(request, os.path.join("artist", "profile_show.html"), context)


@login_required()
def company(request, id):
    objects = get_objects_from_models(COMPANY_PROFILE_MODELS, id)
    objects = remove_elements_by_keys_recursive(objects, ["id", "user", "user_id"])
    objects = remove_pattern_dict_keys(objects, "company")
    context = CONTEXT_TEMPLATE
    context["role"] = request.user.role
    context["objects"] = objects
    context["templates_models"]["company"] = os.path.join(
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
    return render(request, os.path.join("company", "profile_show.html"), context)

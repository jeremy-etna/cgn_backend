import os

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from users.services.objects_manager import (
    get_objects_from_models,
    remove_elements_by_keys_recursive,
    get_templates,
)

from users.services.models_selector import (
    CONTEXT_TEMPLATE,
    COMPANY_PROFILE_MODELS,
    COMPANY_PROFILE_FORMS,
    ARTIST_PROFILE_MODELS,
    ARTIST_PROFILE_FORMS,
)


@login_required()
def profile(request):
    objects = get_objects_from_models(COMPANY_PROFILE_MODELS, request.user.id)
    objects = remove_elements_by_keys_recursive(objects, ["id", "user", "user_id"])
    context = CONTEXT_TEMPLATE
    context["role"] = request.user.role
    context["objects"] = objects
    context["templates_models"]["company"] = os.path.join(
        "company", "components", "company.html"
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
        str(form.__name__).replace('Company', '', 1).replace("Form", "").lower()
        for form in COMPANY_PROFILE_FORMS
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
            return HttpResponseRedirect("../")
        else:
            return render(request, "profile_edit.html", self.context)


@login_required()
def artists(request):
    objects = get_all_objects_from_models(ARTIST_PROFILE_MODELS)
    objects = remove_elements_by_keys_recursive(objects, ["id", "user", "user_id"])
    objects = remove_pattern_dict_keys(objects, "artist")
    print(objects)
    context = CONTEXT_TEMPLATE
    context["role"] = request.user.role
    context["objects"] = objects

    paginator = Paginator(artists_list, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context["objects"] = page_obj
    context["templates_ui"]["artist_card"] = os.path.join(
        "artist", "components", "artist_card.html"
    )
    context["templates_ui"]["paginator"] = os.path.join(
        "common", "components", "paginator.html"
    )

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

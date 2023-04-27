import os

from django.apps import apps
from django.forms.models import model_to_dict
from cgnetwork.settings import BASE_DIR

# PATH MODEL => "{app}/{role}/component/{component}.html"

class ContextBuilder:
    def __init__(self, user):
        self.role = user.user_role
        self.user_id = user.id
        self.models = []
        self.objects = {}
        self.templates = {}
        self.forms = {}

        self.templates['models'] = {}
        self.templates['ui'] = {}

    def _resolve_template_from_component(self, component: str) -> str:
        return os.path.join(self.role, "components", f"{component}.html")

    def _check_template_exists(self, app: str, template: str) -> bool:
        absolute_path = os.path.join(BASE_DIR, app, "templates", template)
        return os.path.exists(absolute_path)

    def _modify_template_root(self, app: str, template: str) -> str:
        return os.path.join(
            BASE_DIR, app, "templates", template.replace(self.role, "common")
        )

    def get_models_templates(self, app: str, components: list) -> dict:
        for component in components:
            template = self._resolve_template_from_component(component)
            if self._check_template_exists(app, template):
                self.templates['models'][component] = template
            else:
                common_template = self._modify_template_root(app, template)
                if self._check_template_exists(app, common_template):
                    self.templates['models'][component] = common_template
                else:
                    raise ValueError(f"Le template '{template}' n'a pas été trouvé.")
        return self.templates['models']

    def get_ui_templates(self, app: str, components: list) -> dict:
        for component in components:
            template = self._resolve_template_from_component(component)
            if self._check_template_exists(app, template):
                self.templates['ui'][component] = template
            else:
                common_template = self._modify_template_root(app, template)
                if self._check_template_exists(app, common_template):
                    self.templates['ui'][component] = common_template
                else:
                    raise ValueError(f"Le template '{template}' n'a pas été trouvé.")
        return self.templates['ui']

    def _resolve_model_form_from_component_name(self, component: str, forms: dict):
        form_name = f"{self.role.capitalize()}, {component.capitalize()}Form"
        try:
            form = forms[form_name]
        except KeyError:
            raise ValueError(f"Le formulaire '{component}' n'a pas été trouvé.")
        return form

    def get_forms(self, components: list, forms: dict) -> dict:
        self.forms = {
            component: self._resolve_model_form_from_component_name(component, forms)
            for component in components
        }
        return self.forms

    def get_models_by_name(self, app_list, components):
        for component in components:
            model_name = f"{component.capitalize()}"
            for app_name in app_list:
                try:
                    model = apps.get_model(app_name, model_name)
                    break
                except LookupError:
                    continue
            if model is None:
                raise ValueError(f"Le modèle '{model_name}' est introuvable.")
            self.models.append(model)
        return self.models

    def get_objects_by_name(self):
        for model in self.models:
            try:
                self.objects[model.__name__.lower()] = model.objects.get(id=self.user_id).__dict__
            except model.DoesNotExist:
                raise ValueError(f"Le modèle '{model.__name__}' est introuvable.")
        return self.objects

    def convert_objects_to_dict(self):
        for name, obj in self.objects.items():
            self.objects[name] = self.django_obj_to_dict(obj, ['id'])
        return self.objects

    def get_context(self) -> dict:
        return {
            "user_role": self.role,
            "objects": self.objects,
            "templates": {
                'models': self.templates['models'],
                'ui': self.templates['ui'],
            },
            "forms": self.forms,
        }


class ModelProcessor:
    def __init__(self, models, user_id, exclude_fields=None):
        self.models = models
        self.user_id = user_id
        self.objects = {}
        if exclude_fields is None:
            self.exclude_fields = []
        else:
            self.exclude_fields = exclude_fields

    def get_objects_by_user_id(self):
        for model in self.models:
            try:
                self.objects[model.__name__.lower()] = model.objects.get(id=self.user_id)
            except model.DoesNotExist:
                raise ValueError(f"Le modèle '{model.__name__}' est introuvable.")
        return self.objects

    def convert_objects_to_dict(self):
        for name, obj in self.objects.items():
            self.objects[name] = model_to_dict(obj, exclude=self.exclude_fields)
        return self.objects

    def process_models(self):
        self.get_objects_by_user_id()
        return self.convert_objects_to_dict()
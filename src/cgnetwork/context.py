import os
import re

from django.apps import apps
from django.forms.models import model_to_dict
from django.utils.module_loading import import_string

from cgnetwork.settings import BASE_DIR


class TemplateResolver:
    def __init__(self, role):
        self.role = role

    def _resolve_template_from_component(self, app: str, component: str) -> str:
        relative_path = os.path.join(app, "templates", self.role, "components", f"{component}.html")
        return os.path.join(BASE_DIR, relative_path)

    def _check_template_exists(self, template: str) -> bool:
        return os.path.exists(template)

    def _modify_template_root(self, app: str, template: str) -> str:
        return os.path.join(
            BASE_DIR, app, "templates", template.replace(self.role, "common")
        )

    def get_templates(self, app: str, components: list, template_type: str) -> dict:
        templates = {}
        for component in components:
            template = self._resolve_template_from_component(app, component)
            if self._check_template_exists(template):
                templates[component] = template
            else:
                common_template = self._modify_template_root(app, template)
                if self._check_template_exists(common_template):
                    templates[component] = common_template
                else:
                    raise ValueError(f"Le template '{template}' n'a pas été trouvé.")
        return templates


# class FormResolver:
#     def __init__(self, role):
#         self.role = role
#
#     def _resolve_model_form_from_component_name(self, component: str, forms: dict):
#         form_name = f"{self.role.capitalize()}, {component.capitalize()}Form"
#         try:
#             form = forms[form_name]
#         except KeyError:
#             raise ValueError(f"Le formulaire '{component}' n'a pas été trouvé.")
#         return form
#
#     def get_forms(self, components: list, forms: dict) -> dict:
#         return {
#             component: self._resolve_model_form_from_component_name(component, forms)
#             for component in components
#         }


class FormResolver:
    def __init__(self, role: str, app_name: str):
        self.role = role
        self.app_name = app_name

    def _resolve_form_from_component_name(self, component: str):
        # Remplacez les caractères de soulignement par des majuscules
        component_name = re.sub(r'_([a-z])', lambda match: match.group(1).upper(), component)
        form_name = f"{self.role.capitalize()}{component_name.capitalize()}Form"
        try:
            form = import_string(f"{self.app_name}.forms.{self.role}.{form_name}")
        except ImportError:
            raise ValueError(f"Le formulaire {form_name} n'a pas été trouvé.")
        return form

    def get_forms(self, components: list) -> dict:
        return {
            component: self._resolve_form_from_component_name(component)
            for component in components
        }


class ModelResolver:
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


class ObjectResolver:
    def __init__(self, role, user_id):
        self.role = role
        self.user_id = user_id
        self.models = []
        self.objects = {}

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

    def get_objects_by_name(self, app_list, components):
        self.get_models_by_name(app_list, components)
        for model in self.models:
            obj = model.objects.get(user_id=self.user_id)
            if obj:
                field_values = {field.name: getattr(obj, field.name) for field in model._meta.fields if
                                field.name not in ('id', 'user')}
                self.objects[model.__name__] = field_values
        return self.objects


class ContextBuilder:
    def __init__(self, user):
        self.role = user.user_role
        self.user_id = user.id
        self.template_resolver = TemplateResolver(self.role)
        self.form_resolver = FormResolver(self.role)
        self.object_resolver = ObjectResolver(self.role, self.user_id)

    def get_models_templates(self, app: str, components: list) -> dict:
        return self.template_resolver.get_templates(app, components, 'models')

    def get_ui_templates(self, app: str, components: list) -> dict:
        return self.template_resolver.get_templates(app, components, 'ui')

    def get_forms(self, components: list, forms: dict) -> dict:
        return self.form_resolver.get_forms(components, forms)

    def get_objects_by_name(self, app_list, components):
        self.object_resolver.get_models_by_name(app_list, components)
        return self.object_resolver.get_objects_by_name()

    def get_context(self) -> dict:
        return {
            "user_role": self.role,
            "objects": self.get_objects_by_name,
            "templates": {
                'models': self.get_models_templates,
                'ui': self.get_ui_templates,
            },
            "forms": self.get_forms,
        }

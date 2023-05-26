import os
from typing import List, Type, Dict, Any, Union
from django.forms.models import model_to_dict
from django.conf import settings


def get_objects_from_models(models: List[Type], user_id: int) -> Dict[str, Any]:
    """
    Retrieves objects from specified Django models based on the user's ID.

    :param models: A list of Django models.
    :param user_id: The ID of the user.
    :return: A dictionary containing the retrieved objects, with the model names as keys.
    """
    objects = {}

    for index, model in enumerate(models):
        model_name = model.__name__.lower()
        objects[model_name] = model_to_dict(model.objects.get(user_id=user_id))

    return objects


def get_all_objects_from_models(models: List[Type]) -> Dict[str, Any]:
    """
    Retrieves all objects from the specified Django models.

    :param models: A list of Django models.
    :return: A dictionary containing the retrieved objects, with the model names as keys.
    """

    objects = {}

    for model in models:
        model_name = model.__name__.lower()
        objects[model_name] = [model_to_dict(obj) for obj in model.objects.all()]

    return objects


def remove_elements_by_keys_recursive(
    dictionary: Dict[str, Any], keys_to_remove: Union[str, List[str]]
) -> Dict[str, Any]:
    """
    Recursively removes elements from a dictionary based on their keys.

    :param dictionary: The dictionary from which to remove the elements.
    :param keys_to_remove: The keys of the elements to remove, either as a string or as a list of strings.
    :return: A new dictionary without the elements whose keys are specified.
    """

    if not isinstance(keys_to_remove, list):
        keys_to_remove = [keys_to_remove]

    new_dictionary = {}

    for key, value in dictionary.items():
        if key not in keys_to_remove:
            if isinstance(value, dict):
                new_dictionary[key] = remove_elements_by_keys_recursive(
                    value, keys_to_remove
                )
            else:
                new_dictionary[key] = value

    return new_dictionary


def get_templates(role: str, components: list) -> dict:
    """
    Generates templates paths based on role and components.

    :param role: User's role
    :param components: List of component names
    :return: A dictionary with component names as keys and their template paths as values.
    """

    return {
        component: f"{role}/components/{component}.html" for component in components
    }


def get_template(app: str, role: str, component: str) -> str:
    """
    Generates a full path to a template based on the application name, role, and component.

    :param app: Name of the Django application.
    :param role: User's role.
    :param component: Name of the component.
    :return: A full path to the desired template.
    """

    return os.path.join(
        settings.BASE_DIR, app, "templates", role, "components", component
    )


def remove_pattern_dict_keys(dictionary: dict, pattern: dict) -> dict:
    """
    Removes a pattern from dictionary keys.

    :param dictionary: The dictionary to modify.
    :param pattern: The pattern to remove from the keys.
    :return: A new dictionary with the modified keys.
    """

    new_dictionary = {}
    for key_name, value in dictionary.items():
        new_dictionary[key_name.replace(pattern, "")] = value
    return new_dictionary

from typing import List, Type, Dict, Any, Union
from django.forms.models import model_to_dict


def get_objects_from_models(models: List[Type], user_id: int) -> Dict[str, Any]:
    """
    Récupère les objets des modèles Django spécifiés en fonction de l'ID de l'utilisateur.

    :param models: Une liste de modèles Django.
    :param user_id: L'ID de l'utilisateur.
    :return: Un dictionnaire contenant les objets récupérés, avec les noms des modèles comme clés.
    """
    objects = {}

    for model in models:
        model_name = model.__name__.lower()
        objects[model_name] = model_to_dict(model.objects.get(user_id=user_id))

    return objects


def get_all_objects_from_models(models: List[Type]) -> Dict[str, Any]:
    """
    Récupère tous les objets des modèles Django spécifiés.

    :param models: Une liste de modèles Django.
    :return: Un dictionnaire contenant les objets récupérés, avec les noms des modèles comme clés.
    """
    objects = {}

    for model in models:
        model_name = model.__name__.lower()
        objects[model_name] = [model_to_dict(obj) for obj in model.objects.all()]

    return objects


def remove_elements_by_keys_recursive(dictionary: Dict[str, Any], keys_to_remove: Union[str, List[str]]) -> Dict[
    str, Any]:
    """
    Supprime récursivement les éléments d'un dictionnaire en fonction de leurs clés.

    :param dictionary: Le dictionnaire à partir duquel supprimer les éléments.
    :param keys_to_remove: Les clés des éléments à supprimer, soit sous forme de chaîne, soit sous forme de liste de chaînes.
    :return: Un nouveau dictionnaire sans les éléments dont les clés sont spécifiées.
    """
    if not isinstance(keys_to_remove, list):
        keys_to_remove = [keys_to_remove]

    new_dictionary = {}

    for key, value in dictionary.items():
        if key not in keys_to_remove:
            if isinstance(value, dict):
                new_dictionary[key] = remove_elements_by_keys_recursive(value, keys_to_remove)
            else:
                new_dictionary[key] = value

    return new_dictionary


def get_templates_from_models(models: list[type], role: str) -> dict:
    return {
        model.__name__.lower(): f"{role}/components/{model.__name__.lower()}.html"
        for model in models
    }


def get_templates(role: str, components: list) -> dict:
    return {
        component: f"{role}/components/{component}.html" for component in components
    }

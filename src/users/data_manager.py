from typing import List, Tuple, Type

from cgnetwork.models import (
    Coordinate,
    Contract,
    Mobility,
    Administrative,
    SocialMedia,
    Sector,
    Competence,
    Software,
    CompanyCompetence,
    CompanySoftware,
)
from users.models.artist import Artist
from users.models.company import Company


def get_profile_data(user_id: int, models: List[Tuple[Type, str]]) -> dict:
    context = {}
    for model, context_key in models:
        context[context_key] = model.objects.get(user_id=user_id)
    return context


def get_artist_profile_data(user_id: int) -> dict:
    models = [
        (Artist, "identity"),
        (Coordinate, "coordinate"),
        (Contract, "contract"),
        (Mobility, "mobility"),
        (Administrative, "administrative"),
        (SocialMedia, "socialMedia"),
        (Sector, "sector"),
        (Competence, "competence"),
        (Software, "software"),
    ]
    return get_profile_data(user_id, models)


def get_company_profile_data(user_id: int) -> dict:
    models = [
        (Company, "identity"),
        (Coordinate, "coordinate"),
        (Mobility, "mobility"),
        (SocialMedia, "socialMedia"),
        (Sector, "sector"),
        (CompanyCompetence, "competence"),
        (CompanySoftware, "software"),
    ]
    return get_profile_data(user_id, models)


def convert_objects_to_dict(context: dict) -> dict:
    for key, obj in context.items():
        if hasattr(obj, "__dict__"):
            context[key] = {
                field.name: getattr(obj, field.name)
                for field in obj._meta.fields
                if field.name not in ("id", "user")
            }
    return context


def get_templates(role: str, components: list) -> dict:
    return {
        component: f"{role}/components/{component}.html" for component in components
    }

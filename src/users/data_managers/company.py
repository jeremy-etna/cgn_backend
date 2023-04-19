from cgnetwork.models import (
    Coordinate,
    Mobility,
    SocialMedia,
    Sector,
    CompanyCompetence,
    CompanySoftware,
)
from users.models.company import Company


def get_profile_data(user_id: int) -> dict:
    models = [
        (Company, 'identity'),
        (Coordinate, 'coordinate'),
        (Mobility, 'mobility'),
        (SocialMedia, 'socialMedia'),
        (Sector, 'sector'),
        (CompanyCompetence, 'competence'),
        (CompanySoftware, 'software'),
    ]
    context = {}
    for model, context_key in models:
        context[context_key] = model.objects.get(user_id=user_id)
    return context


def convert_objects_to_dict(context: dict) -> dict:
    for key, obj in context.items():
        if hasattr(obj, '__dict__'):
            context[key] = {
                field.name: getattr(obj, field.name)
                for field in obj._meta.fields
                if field.name not in ('id', 'user')
            }
    return context


def get_templates(role: str, components: list) -> dict:
    context = {}
    for component in components:
        path = f"{role}/components/{component}.html"
        context[component] = path
    return context

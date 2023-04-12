from cgnetwork.models import (
    Coordinate,
    Contract,
    Mobility,
    Administrative,
    SocialMedia,
    Sector,
    Competence,
    Software,
)
from users.models.company import Company


def get_profile_data(user_id: int) -> dict:
    models = [
        (Company, 'identity'),
        (Coordinate, 'coordinate'),
        (Mobility, 'mobility'),
        (Administrative, 'administrative'),
        (SocialMedia, 'socialMedia'),
        (Sector, 'sector'),
        (Competence, 'competence'),
        (Software, 'software'),
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
from django.contrib import admin

from users.models.common import CustomUser
from users.services.models_selector import (
    ARTIST_PROFILE_MODELS,
    COMPANY_PROFILE_MODELS,
)


admin.site.register(CustomUser)

for model in ARTIST_PROFILE_MODELS:
    admin.site.register(model)

for model in COMPANY_PROFILE_MODELS:
    admin.site.register(model)


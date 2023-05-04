from users.models.artist import Artist
from users.models.company import (
    Company,
    Competence,
    Software,
)
from users.models.common import (
    Coordinate,
    Administrative,
    Mobility,
    SocialMedia,
    Contract,
    Sector,
    Competence,
    Software,
)

from users.forms.artist import (
    ArtistArtistForm,
    ArtistCoordinateForm,
    ArtistAdministrativeForm,
    ArtistMobilityForm,
    ArtistSocialMediaForm,
    ArtistContractForm,
    ArtistSectorForm,
    ArtistCompetenceForm,
    ArtistSoftwareForm,
)

from users.forms.company import (
    CompanyCompanyForm,
    CompanyCoordinateForm,
    CompanyMobilityForm,
    CompanySocialMediaForm,
    CompanySectorForm,
    CompanyCompetenceForm,
    CompanySoftwareForm,
)

CONTEXT_TEMPLATE = {
    "role": "",
    "objects": {},
    "forms": {},
    "templates_models": {},
    "templates_ui": {},
}

ARTIST_PROFILE_MODELS = [
    Artist,
    Coordinate,
    Administrative,
    Mobility,
    SocialMedia,
    Contract,
    Sector,
    Competence,
    Software,
]

ARTIST_PROFILE_FORMS = [
    ArtistArtistForm,
    ArtistCoordinateForm,
    ArtistAdministrativeForm,
    ArtistMobilityForm,
    ArtistSocialMediaForm,
    ArtistContractForm,
    ArtistSectorForm,
    ArtistCompetenceForm,
    ArtistSoftwareForm,
]

COMPANY_PROFILE_MODELS = [
    Company,
    Coordinate,
    Mobility,
    SocialMedia,
    Sector,
    CompanyCompetence,
    CompanySoftware,
]

COMPANY_PROFILE_FORMS = [
    CompanyCompanyForm,
    CompanyCoordinateForm,
    CompanyMobilityForm,
    CompanySocialMediaForm,
    CompanySectorForm,
    CompanyCompetenceForm,
    CompanySoftwareForm,
]
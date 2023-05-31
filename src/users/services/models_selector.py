from users.models.artist import (
    ArtistIdentity,
    ArtistCoordinate,
    ArtistAdministrative,
    ArtistMobility,
    ArtistSocialMedia,
    ArtistContract,
    ArtistSector,
    ArtistCompetence,
    ArtistSoftware,
)

from users.models.company import (
    CompanyIdentity,
    CompanyCoordinate,
    CompanyMobility,
    CompanySocialMedia,
    CompanySector,
    CompanyCompetence,
    CompanySoftware,
)

from users.forms.artist import (
    ArtistIdentityForm,
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
    CompanyIdentityForm,
    CompanyCoordinateForm,
    CompanyMobilityForm,
    CompanySocialMediaForm,
    CompanySectorForm,
    CompanyCompetenceForm,
    CompanySoftwareForm,
)


ARTIST_PROFILE_MODELS = [
    ArtistIdentity,
    ArtistCoordinate,
    ArtistAdministrative,
    ArtistMobility,
    ArtistSocialMedia,
    ArtistContract,
    ArtistSector,
    ArtistCompetence,
    ArtistSoftware,
]

ARTIST_PROFILE_FORMS = [
    ArtistIdentityForm,
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
    CompanyIdentity,
    CompanyCoordinate,
    CompanyMobility,
    CompanySocialMedia,
    CompanySector,
    CompanyCompetence,
    CompanySoftware,
]

COMPANY_PROFILE_FORMS = [
    CompanyIdentityForm,
    CompanyCoordinateForm,
    CompanyMobilityForm,
    CompanySocialMediaForm,
    CompanySectorForm,
    CompanyCompetenceForm,
    CompanySoftwareForm,
]
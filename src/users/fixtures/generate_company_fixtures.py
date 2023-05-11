import os
import json
import random
from faker import Faker

from cgnetwork.constants.models import (
    MOBILITIES,
    WEBSITES,
    SECTORS,
    COMPETENCES,
    SOFTWARES,
)

fake = Faker()

instance_start = 31
instance_end = 60

company_identities = []
company_coordinates = []
company_mobilities = []
company_social_medias = []
company_sectors = []
company_competences = []
company_softwares = []

import os


def list_files(directory):
    files = []
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path):
            files.append(file_name)
    return files


logos = list_files("../../media/logos")

for i in range(instance_start, instance_end + 1):
    company_identities.append(
        {
            "model": "users.companyidentity",
            "pk": i-30,
            "fields": {
                "user": i,
                "avatar": f"logos/{logos[i-30]}",
                "company_name": fake.company(),
                "description": fake.text(max_nb_chars=200),
            },
        }
    )

    company_coordinates.append(
        {
            "model": "users.companycoordinate",
            "pk": i-30,
            "fields": {
                "user": i,
                "country": fake.country(),
                "state": fake.state(),
                "city": fake.city(),
                "zip_code": fake.zipcode(),
                "street_name": fake.street_name(),
                "street_number": fake.building_number(),
                "phone_number": fake.phone_number(),
            },
        }
    )

    mobility_fields = {
        mobility: fake.boolean(chance_of_getting_true=50) for mobility in MOBILITIES
    }
    company_mobilities.append(
        {
            "model": "users.companymobility",
            "pk": i-30,
            "fields": {
                "user": i,
                **mobility_fields,
            },
        }
    )

    website_fields = {
        website: fake.url() if fake.boolean(chance_of_getting_true=50) else ""
        for website in WEBSITES
    }
    company_social_medias.append(
        {
            "model": "users.companysocialmedia",
            "pk": i-30,
            "fields": {
                "user": i,
                **website_fields,
            },
        }
    )

    sector_fields = {
        sector: fake.boolean(chance_of_getting_true=50) for sector in SECTORS
    }
    company_sectors.append(
        {
            "model": "users.companysector",
            "pk": i-30,
            "fields": {
                "user": i,
                **sector_fields,
            },
        }
    )

    competence_fields = {
        competence: random.choice([True, False]) for competence in COMPETENCES
    }
    company_competences.append(
        {
            "model": "users.companycompetence",
            "pk": i-30,
            "fields": {
                "user": i,
                **competence_fields,
            },
        }
    )

    software_fields = {
        software: random.choice([True, False]) for software in SOFTWARES
    }
    company_softwares.append(
        {
            "model": "users.companysoftware",
            "pk": i-30,
            "fields": {
                "user": i,
                **software_fields,
            },
        }
    )


with open("company_fixtures.json", "w") as file:
    json.dump(
        company_identities
        + company_coordinates
        + company_mobilities
        + company_social_medias
        + company_sectors
        + company_competences
        + company_softwares,
        file,
        indent=4,
    )

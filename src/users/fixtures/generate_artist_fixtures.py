import os
import sys
import json
import random
from faker import Faker

import django
sys.path.append(r'D:\RNCP\cg_network\src')
os.environ['DJANGO_SETTINGS_MODULE'] = 'cgnetwork.settings'
django.setup()

from cgnetwork.constants.models import (
    COMPETENCES,
    MOBILITIES,
    CONTRACTS,
    WEBSITES,
    SECTORS,
    SOFTWARES,
    SkillLevel,
)

fake = Faker()

instance_start = 1
instance_end = 30

artist_identities = []
artist_coordinates = []
artist_administratives = []
artist_contracts = []
artist_mobilities = []
artist_social_medias = []
artist_sectors = []
artist_competences = []
artist_softwares = []

for i in range(instance_start, instance_end + 1):
    artist_identities.append(
        {
            "model": "users.artistidentity",
            "pk": i,
            "fields": {
                "user": i,
                "avatar": f"avatars/portrait_{i}.jpg",
                "title": fake.job(),
                "first_name": fake.first_name(),
                "last_name": fake.last_name(),
                "description": fake.text(max_nb_chars=200),
            },
        }
    )

    artist_coordinates.append(
        {
            "model": "users.artistcoordinate",
            "pk": i,
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

    artist_administratives.append(
        {
            "model": "users.artistadministrative",
            "pk": i,
            "fields": {
                "user": i,
                "spectacle_number": fake.numerify(text="########"),
                "siret_number": fake.numerify(text="##############"),
                "price": fake.random_number(digits=3),
            },
        }
    )

    contract_fields = {
        contract: fake.boolean(chance_of_getting_true=50) for contract in CONTRACTS
    }
    artist_contracts.append(
        {
            "model": "users.artistcontract",
            "pk": i,
            "fields": {
                "user": i,
                **contract_fields,
            },
        }
    )

    mobility_fields = {
        mobility: fake.boolean(chance_of_getting_true=50) for mobility in MOBILITIES
    }
    artist_mobilities.append(
        {
            "model": "users.artistmobility",
            "pk": i,
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
    artist_social_medias.append(
        {
            "model": "users.artistsocialmedia",
            "pk": i,
            "fields": {
                "user": i,
                **website_fields,
            },
        }
    )

    sector_fields = {
        sector: fake.boolean(chance_of_getting_true=50) for sector in SECTORS
    }
    artist_sectors.append(
        {
            "model": "users.artistsector",
            "pk": i,
            "fields": {
                "user": i,
                **sector_fields,
            },
        }
    )

    competence_fields = {
        competence: random.choice(SkillLevel.values) for competence in COMPETENCES
    }
    artist_competences.append(
        {
            "model": "users.artistcompetence",
            "pk": i,
            "fields": {
                "user": i,
                **competence_fields,
            },
        }
    )

    software_fields = {
        software: random.choice(SkillLevel.values) for software in SOFTWARES
    }
    artist_softwares.append(
        {
            "model": "users.artistsoftware",
            "pk": i,
            "fields": {
                "user": i,
                **software_fields,
            },
        }
    )


with open("artist_fixtures.json", "w") as file:
    json.dump(
        artist_identities
        + artist_coordinates
        + artist_administratives
        + artist_contracts
        + artist_mobilities
        + artist_social_medias
        + artist_sectors
        + artist_competences
        + artist_softwares,
        file,
        indent=4,
    )

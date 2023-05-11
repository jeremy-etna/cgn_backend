import json
import random
from faker import Faker

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cgnetwork.settings")
import django
django.setup()

from django.contrib.auth.models import Group

fake = Faker()

num_users = 60
output_file = "customuser_data.json"

custom_users = []

group_ids = list(Group.objects.values_list("id", flat=True))

for i in range(1, num_users + 1):
    email = fake.email()
    password = fake.password()
    is_active = random.choice([True, False])
    is_staff = random.choice([True, False])
    if i <= 30:
        role = "artist"
    else:
        role = "company"

    custom_users.append({
        "model": "users.customuser",
        "pk": i,
        "fields": {
            "password": password,
            "last_login": None,
            "email": fake.email(),
            "register_date": fake.date_between(start_date="-5y", end_date="today").isoformat(),
            "is_active": True,
            "is_staff": False,
            "role": role
        }
    })

with open("customuser_fixtures.json", "w") as f:
    json.dump(custom_users, f)

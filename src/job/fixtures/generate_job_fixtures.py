import json
from faker import Faker

fake = Faker()

num_jobs = 20
output_file = "job_data.json"

jobs = []

for i in range(1, num_jobs + 1):

    jobs.append({
        "model": "job.job",
        "pk": i,
        "fields": {
            "user": fake.random_int(min=31, max=60),
            "company": fake.random_int(min=1, max=30),
            "creation_date": fake.date_between(start_date="-5y", end_date="today").isoformat(),
            "title": fake.job(),
            "company_description": ''.join(fake.sentences(nb=11, ext_word_list=None)) + '. ',
            "job_responsibilities": ''.join(fake.sentences(nb=11, ext_word_list=None)) + '. ',
            "required_skills": ''.join(fake.sentences(nb=11, ext_word_list=None)) + '. ',
            "required_qualifications": ''.join(fake.sentences(nb=11, ext_word_list=None)) + '. ',
            "job_requirements": ''.join(fake.sentences(nb=11, ext_word_list=None)) + '. ',
            "employee_benefits": ''.join(fake.sentences(nb=11, ext_word_list=None)) + '. ',
            "salary_min": fake.random_int(min=10, max=20) * 10,
            "salary_max": fake.random_int(min=30, max=40) * 10,
            "views": fake.random_number(digits=2)
        }
    })

with open("job_fixtures.json", "w") as f:
    json.dump(jobs, f)

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'internship_hub_project.settings')

import django
django.setup()

from forum.models import Company, Vacancy

def populate():
    c = Company.objects.get_or_create(
        name="Google",
        description="Tech company",
        website="https://google.com"
    )[0]

    Vacancy.objects.get_or_create(
        company=c,
        title="Software Intern",
        description="Internship role",
        industry="Tech",
        job_type="Internship",
        salary="Paid",
        url="https://google.com",
        location="London"
    )

if __name__ == '__main__':
    populate()
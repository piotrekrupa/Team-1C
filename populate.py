import os
import django
from datetime import timedelta

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "internship_hub_project.settings")
django.setup()

from django.utils import timezone
from forum.models import Company, Vacancy


def add_company_with_vacancies(company_data, vacancies):
    company, created = Company.objects.get_or_create(
        name=company_data["name"],
        defaults={
            "description": company_data["description"],
            "website": company_data["website"],
        },
    )

    for vacancy in vacancies:
        Vacancy.objects.get_or_create(
            company=company,
            title=vacancy["title"],
            defaults={
                "description": vacancy["description"],
                "salary": vacancy["salary"],
                "location": vacancy["location"],
                "deadline": timezone.now().date() + timedelta(days=vacancy["days_until_deadline"]),
                "url": vacancy["url"],
                "job_type": vacancy["job_type"],
            },
        )

    print(f"Added data for {company.name}")


def populate():
    companies = [
        {
            "company": {
                "name": "Trackr",
                "description": "A UK internships and opportunities platform focused on helping students discover graduate roles, placements, and summer internships.",
                "website": "https://app.the-trackr.com",
            },
            "vacancies": [
                {
                    "title": "Software Engineering Intern",
                    "description": "Support the development of internship search and analytics features for students and early-career applicants.",
                    "salary": "2500",
                    "location": "Bristol",
                    "days_until_deadline": 30,
                    "url": "https://app.the-trackr.com/uk-technology/summer-internships",
                    "job_type": "Internship",
                },
                {
                    "title": "Product Data Intern",
                    "description": "Help maintain and analyse internship listings and improve platform data quality.",
                    "salary": "2200",
                    "location": "Remote",
                    "days_until_deadline": 45,
                    "url": "https://app.the-trackr.com/uk-technology/summer-internships",
                    "job_type": "Internship",
                },
            ],
        },
        {
            "company": {
                "name": "Arm",
                "description": "A semiconductor and software design company known for processor architecture and technology innovation.",
                "website": "https://www.arm.com",
            },
            "vacancies": [
                {
                    "title": "Embedded Systems Intern",
                    "description": "Work with engineers on processor-based systems, testing, and performance analysis.",
                    "salary": "2800",
                    "location": "Cambridge",
                    "days_until_deadline": 40,
                    "url": "https://www.arm.com",
                    "job_type": "Internship",
                },
                {
                    "title": "Hardware Validation Engineer",
                    "description": "Assist with validation and verification tasks for cutting-edge computing platforms.",
                    "salary": "3200",
                    "location": "Manchester",
                    "days_until_deadline": 50,
                    "url": "https://www.arm.com",
                    "job_type": "Job",
                },
            ],
        },
        {
            "company": {
                "name": "Ocado Technology",
                "description": "A technology business building software, robotics, and systems for online retail and logistics.",
                "website": "https://www.ocadotechnology.com",
            },
            "vacancies": [
                {
                    "title": "Backend Developer",
                    "description": "Contribute to scalable backend services supporting e-commerce and logistics systems.",
                    "salary": "2600",
                    "location": "London",
                    "days_until_deadline": 35,
                    "url": "https://www.ocadotechnology.com",
                    "job_type": "Job",
                },
                {
                    "title": "Data Science Intern",
                    "description": "Support analytics and machine learning work for forecasting and operational optimisation.",
                    "salary": "2550",
                    "location": "Hatfield",
                    "days_until_deadline": 42,
                    "url": "https://www.ocadotechnology.com",
                    "job_type": "Internship",
                },
            ],
        },
        {
            "company": {
                "name": "NovaStack Solutions",
                "description": "A fictional software consultancy delivering cloud, web, and mobile solutions to growing businesses.",
                "website": "https://www.novastacksolutions.com",
            },
            "vacancies": [
                {
                    "title": "Full-Stack Developer",
                    "description": "Build and test modern web applications across frontend and backend components.",
                    "salary": "2900",
                    "location": "Glasgow",
                    "days_until_deadline": 28,
                    "url": "https://www.novastacksolutions.com/careers",
                    "job_type": "Job",
                },
                {
                    "title": "QA Automation Intern",
                    "description": "Write test scripts and support automated quality assurance pipelines.",
                    "salary": "1900",
                    "location": "Remote",
                    "days_until_deadline": 38,
                    "url": "https://www.novastacksolutions.com/careers",
                    "job_type": "Internship",
                },
            ],
        },
        {
            "company": {
                "name": "BrightPath Digital",
                "description": "A fictional digital agency focused on product design, UX, and data-led growth.",
                "website": "https://www.brightpathdigital.co.uk",
            },
            "vacancies": [
                {
                    "title": "UX/UI Design Intern",
                    "description": "Create wireframes, prototypes, and interface ideas for client-facing products.",
                    "salary": "1850",
                    "location": "Edinburgh",
                    "days_until_deadline": 32,
                    "url": "https://www.brightpathdigital.co.uk/careers",
                    "job_type": "Job",
                },
                {
                    "title": "Digital Marketing Executive",
                    "description": "Support campaign analysis, SEO tasks, and digital growth strategies.",
                    "salary": "2400",
                    "location": "Remote",
                    "days_until_deadline": 36,
                    "url": "https://www.brightpathdigital.co.uk/careers",
                    "job_type": "Job",
                },
            ],
        },
        {
            "company": {
                "name": "FinCore Analytics",
                "description": "A fictional fintech company providing analytics, dashboards, and reporting tools for financial teams.",
                "website": "https://www.fincoreanalytics.com",
            },
            "vacancies": [
                {
                    "title": "Data Analyst Intern",
                    "description": "Analyse internal datasets and produce reports for stakeholders and product teams.",
                    "salary": "2300",
                    "location": "London",
                    "days_until_deadline": 41,
                    "url": "https://www.fincoreanalytics.com/careers",
                    "job_type": "Internship",
                },
                {
                    "title": "Business Intelligence Analyst",
                    "description": "Support dashboard development and insight generation for financial products.",
                    "salary": "3000",
                    "location": "Birmingham",
                    "days_until_deadline": 44,
                    "url": "https://www.fincoreanalytics.com/careers",
                    "job_type": "Job",
                },
            ],
        },
        {
            "company": {
                "name": "NorthBridge HealthTech",
                "description": "A fictional health technology company building software for patient engagement and operations.",
                "website": "https://www.northbridgehealthtech.com",
            },
            "vacancies": [
                {
                    "title": "Python Developer",
                    "description": "Help develop internal tools and APIs for healthcare workflow products.",
                    "salary": "2850",
                    "location": "Leeds",
                    "days_until_deadline": 34,
                    "url": "https://www.northbridgehealthtech.com/careers",
                    "job_type": "Job",
                },
                {
                    "title": "Product Support Intern",
                    "description": "Assist with product testing, issue tracking, and support documentation.",
                    "salary": "1800",
                    "location": "Remote",
                    "days_until_deadline": 29,
                    "url": "https://www.northbridgehealthtech.com/careers",
                    "job_type": "Job",
                },
            ],
        },
        {
            "company": {
                "name": "Elevate Cloud Systems",
                "description": "A fictional cloud services business helping companies modernise infrastructure and workflows.",
                "website": "https://www.elevatecloudsystems.com",
            },
            "vacancies": [
                {
                    "title": "Cloud Engineer",
                    "description": "Support cloud deployment, monitoring, and infrastructure management tasks.",
                    "salary": "3100",
                    "location": "Manchester",
                    "days_until_deadline": 37,
                    "url": "https://www.elevatecloudsystems.com/careers",
                    "job_type": "Job",
                },
                {
                    "title": "DevOps Intern",
                    "description": "Help improve CI/CD pipelines and deployment automation processes.",
                    "salary": "2350",
                    "location": "Remote",
                    "days_until_deadline": 39,
                    "url": "https://www.elevatecloudsystems.com/careers",
                    "job_type": "Job",
                },
            ],
        },
    ]

    for entry in companies:
        add_company_with_vacancies(entry["company"], entry["vacancies"])

    print("Database populated successfully!")


if __name__ == "__main__":
    print("Starting population script...")
    populate()
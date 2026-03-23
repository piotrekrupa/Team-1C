from django.test import TestCase
from .models import Company

class CompanyTesting(TestCase):
    def test_slug_generation(self):
        company = Company(name="Random Company", description="Search Engine")
        company.save()
        self.assertEqual(company.slug, "random-company")

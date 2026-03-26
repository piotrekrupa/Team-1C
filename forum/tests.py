from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from forum.models import Company, Vacancy, Profile

class ForumTests(TestCase):
    def setUp(self):
        self.company= Company.objects.create(
            name="Cloud Systems",
            description="Testing cloud services",
            website="https://cloudtest.com"
        )

    def test_company_slug_generation(self):
        self.assertEqual(self.company.slug, "cloud-systems")

    def test_vacancy_slug_generation(self):
        vacancy= Vacancy.objects.create(
            company=self.company,
            title="DevOps Engineer",
            description="Test description",
            job_type="entry_level",
            location="Remote"
        )
        self.assertEqual(vacancy.slug, "cloud-systems-devops-engineer")

    def test_profile_creation_on_user_save(self):
        user = User.objects.create_user(username="test", password="webappdev2")
        profile = Profile.objects.create(user=user, full_name="Testing")
        self.assertEqual(profile.user.username, "test")


class ForumViewTests(TestCase):
    def setUp(self):
        self.client= Client()
        self.company= Company.objects.create(name="TechCorp")
        self.vacancy= Vacancy.objects.create(company=self.company,title="Software Intern",
        job_type="Internship",description="Sample intern role")

    def test_home_view_status_code(self):
        response = self.client.get(reverse('forum:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'WAD2/homepage.html')

    def test_internship_list(self):
        response = self.client.get(reverse('forum:internships'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Software Intern")
        self.assertContains(response, "Available Internships")
    def test_vacancy_detail_view(self):
        url = reverse('forum:vacancy', kwargs={'slug': self.vacancy.slug})
        response= self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Software Intern")

class ForumFunctionalTests(TestCase):
    def setUp(self):
        self.company = Company.objects.create(name="DataInc")
        Vacancy.objects.create(
            company=self.company,
            title="Python Developer",
            job_type="entry_level"
        )

    def test_search_functionality(self):
        response = self.client.get(reverse('forum:search'), {'query': 'Python'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Python Developer")

    def test_empty_search_behavior(self):
        response = self.client.get(reverse('forum:search'), {'query': ''})
        self.assertContains(response, "Please enter a search term")
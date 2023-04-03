from django.test import TestCase, Client
from django.urls import reverse



class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.profile_url = reverse('artist-profile')
        self.profile_edit_url = reverse('artist-profile-edit')
        self.jobs_url = reverse('artist-jobs')
        self.job_url = reverse('artist-job')
        self.companies_url = reverse('artist-companies')
        self.company_url = reverse('artist-company')

    def test_profile_GET(self):
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed(response, 'artist/profile.html')

    def test_profile_edit_GET(self):
        response = self.client.get(self.profile_edit_url)
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed(response, 'artist/profile_edit.html')

    # def test_profile_edit_POST(self):
    #     response = self.client.get(self.profile_edit_url)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertTemplateUsed(response, 'artist/profile_edit.html')

    def test_jobs_GET(self):
        response = self.client.get(self.jobs_url)
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed(response, 'artist/jobs.html')

    def test_job_GET(self):
        response = self.client.get(self.job_url)
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed(response, 'artist/job.html')

    def test_companies_GET(self):
        response = self.client.get(self.companies_url)
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed(response, 'artist/companies.html')

    def test_company_GET(self):
        response = self.client.get(self.company_url)
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed(response, 'artist/company.html')
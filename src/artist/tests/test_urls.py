from django.test import SimpleTestCase
from django.urls import reverse, resolve
from artist.views import (
    profile,
    profile_edit,
    jobs,
    companies,
    company,
    job
    )


class TestUrls(SimpleTestCase):

    def test_artist_profile_url_is_resolved(self):
        url = reverse('artist-profile')
        self.assertEquals(resolve(url).func, profile)

    def test_artist_profile_edit_url_is_resolved(self):
        url = reverse('artist-profile-edit')
        self.assertEquals(resolve(url).func, profile_edit)

    def test_artist_jobs_url_is_resolved(self):
        url = reverse('artist-jobs')
        self.assertEquals(resolve(url).func, jobs)

    def test_artist_job_url_is_resolved(self):
        url = reverse('artist-job', args=[1])
        self.assertEquals(resolve(url).func, job)

    def test_artist_companies_url_is_resolved(self):
        url = reverse('artist-companies')
        self.assertEquals(resolve(url).func, companies)

    def test_artist_company_url_is_resolved(self):
        url = reverse('artist-company', args=[1])
        self.assertEquals(resolve(url).func, company)

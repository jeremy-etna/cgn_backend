from django.test import TestCase
from users.forms.company import CompanyIdentityForm
from users.models.company import CompanyIdentity
from cgnetwork.constants.models import CompanySize


class CompanyIdentityFormTest(TestCase):
    def setUp(self):
        self.data = {
            "company_name": "Jeremy Co.",
            "description": "This is a test company",
            "company_size": CompanySize.SIZE_51_99,
        }

    def test_company_identity_form(self):
        form = CompanyIdentityForm(data=self.data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data.get("company_name"), "Jeremy Co.")

    def test_save(self):
        form = CompanyIdentityForm(data=self.data)
        form.is_valid()
        company_identity = form.save(commit=False)
        self.assertIsInstance(company_identity, CompanyIdentity)
        self.assertEqual(company_identity.company_name, "Jeremy Co.")

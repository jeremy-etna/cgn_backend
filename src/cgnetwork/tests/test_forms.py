from django.test import SimpleTestCase
from cgnetwork.forms import UserRegistrationForm


class TestForms(SimpleTestCase):

    def test_UserRegistrationForm_valid_data(self):
        form = UserRegistrationForm(data={
            'role': 'artist',
            'email': 'jeremy@etna.net',
        })
        self.assertTrue(form.is_valid())

    def test_UserRegistrationForm_no_data(self):
        form = UserRegistrationForm(data={})
        self.assertTrue(form.is_valid())

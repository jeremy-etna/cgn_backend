from django.test import TestCase

from users.forms.artist import ArtistIdentityForm
from users.models.artist import ArtistIdentity


class ArtistIdentityFormTest(TestCase):
    def setUp(self):
        self.data = {
            "first_name": "Jeremy",
            "last_name": "Oblet",
        }

    def test_artist_identity_form(self):
        form = ArtistIdentityForm(data=self.data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data.get("first_name"), "Jeremy")
        self.assertEqual(form.cleaned_data.get("last_name"), "Oblet")

    def test_save(self):
        form = ArtistIdentityForm(data=self.data)
        form.is_valid()
        artist_identity = form.save(commit=False)

        self.assertIsInstance(artist_identity, ArtistIdentity)
        self.assertEqual(artist_identity.first_name, "Jeremy")
        self.assertEqual(artist_identity.last_name, "Oblet")

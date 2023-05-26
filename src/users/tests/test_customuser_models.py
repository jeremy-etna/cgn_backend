from django.test import TestCase
from django.utils import timezone
from django.core.exceptions import ValidationError


from users.models import CustomUser
from cgnetwork.constants.models import (
    Role,
)

from users.models.artist import (
    ArtistIdentity,
    ArtistCoordinate,
    ArtistAdministrative,
    ArtistContract,
    ArtistMobility,
    ArtistSocialMedia,
    ArtistSector,
    ArtistCompetence,
    ArtistSoftware,
)

from users.models.company import (
    CompanyIdentity,
    CompanyCoordinate,
    CompanyMobility,
    CompanySocialMedia,
    CompanySector,
    CompanyCompetence,
    CompanySoftware,
)


class CustomUserModelTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(
            email="test@example.com", role=Role.ARTIST
        )

    def test_email_uniqueness(self):
        with self.assertRaises(Exception):
            CustomUser.objects.create(email="test@example.com", role=Role.ARTIST)

    def test_email_presence(self):
        user = CustomUser(email="", role=Role.ARTIST)
        with self.assertRaises(ValidationError):
            user.full_clean()

    def test_default_values(self):
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertTrue(self.user.register_date <= timezone.now())

    def test_has_module_perms(self):
        self.assertFalse(self.user.has_module_perms("any_app_label"))

        self.user.is_staff = True
        self.user.save()

        self.assertTrue(self.user.has_module_perms("any_app_label"))

    def test_has_perm(self):
        self.assertFalse(self.user.has_perm("any_permission"))

        self.user.is_staff = True
        self.user.save()

        self.assertTrue(self.user.has_perm("any_permission"))

    def test_str_representation(self):
        self.assertEqual(str(self.user), "test@example.com")


class CustomUserModelTest(TestCase):
    def test_post_save_receiver_artist(self):
        user = CustomUser.objects.create(email="artist@example.com", role=Role.ARTIST)

        self.assertIsNotNone(ArtistIdentity.objects.filter(user=user).first())
        self.assertIsNotNone(ArtistCoordinate.objects.filter(user=user).first())
        self.assertIsNotNone(ArtistAdministrative.objects.filter(user=user).first())
        self.assertIsNotNone(ArtistContract.objects.filter(user=user).first())
        self.assertIsNotNone(ArtistMobility.objects.filter(user=user).first())
        self.assertIsNotNone(ArtistSocialMedia.objects.filter(user=user).first())
        self.assertIsNotNone(ArtistSector.objects.filter(user=user).first())
        self.assertIsNotNone(ArtistCompetence.objects.filter(user=user).first())
        self.assertIsNotNone(ArtistSoftware.objects.filter(user=user).first())

    def test_post_save_receiver_company(self):
        user = CustomUser.objects.create(email="company@example.com", role=Role.COMPANY)

        self.assertIsNotNone(CompanyIdentity.objects.filter(user=user).first())
        self.assertIsNotNone(CompanyCoordinate.objects.filter(user=user).first())
        self.assertIsNotNone(CompanyMobility.objects.filter(user=user).first())
        self.assertIsNotNone(CompanySocialMedia.objects.filter(user=user).first())
        self.assertIsNotNone(CompanySector.objects.filter(user=user).first())
        self.assertIsNotNone(CompanyCompetence.objects.filter(user=user).first())
        self.assertIsNotNone(CompanySoftware.objects.filter(user=user).first())

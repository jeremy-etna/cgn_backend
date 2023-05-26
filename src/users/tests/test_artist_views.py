from django.test import TestCase, RequestFactory
from users.models.common import CustomUser as User
from users.models.artist import ArtistIdentity
from users.views.artist import profile, ProfileEditView


class ProfileViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            email="test@user.net", password="testpassword"
        )
        self.user.role = "artist"
        self.user.save()
        self.artist_identity = ArtistIdentity.objects.create(
            user=self.user,
            avatar="avatars/artist_default.png",
            first_name="Test",
            last_name="User",
            title="title",
            description="description",
        )

    def test_profile_view(self):
        request = self.factory.get("/profile")
        request.user = self.user

        response = profile(request)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "artist/profile.html")
        self.assertEqual(response.context["role"], self.user.role)


class ProfileEditViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            email="test@user.net", password="testpassword"
        )
        self.user.role = "artist"
        self.user.save()
        self.artist_identity = ArtistIdentity.objects.create(
            user=self.user,
            avatar="avatars/artist_default.png",
            first_name="Test",
            last_name="User",
            title="title",
            description="description",
        )
        self.view = ProfileEditView()

    def test_get(self):
        request = self.factory.get("/profile/edit")
        request.user = self.user

        response = self.view.get(request)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "artist/profile_edit.html")
        self.assertEqual(response.context["role"], self.user.role)

    def test_post(self):
        request = self.factory.post(
            "/profile/edit",
            data={
                "current-form": "ArtistIdentityForm",
                "first_name": "Test",
                "last_name": "User",
            },
        )
        request.user = self.user

        response = self.view.post(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"], "../#identity-section")

        self.user.refresh_from_db()
        self.assertEqual(self.user.artistidentity.first_name, "Test")
        self.assertEqual(self.user.artistidentity.last_name, "User")

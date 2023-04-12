from django.test import TestCase, Client
from django.urls import reverse


class TestArtistModel(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.register_url = reverse('register')
        self.login_url = reverse('login')

    def test_home_GET(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cgnetwork/home.html')

    def test_register_GET(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')

    def test_login_GET(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_register_POST(self):
        response = self.client.post(self.register_url, {
            'user_role': 'artist',
            'email': 'jeremy@etna.net',
            'password1': '123456',
            'password2': '123456'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')

    def test_login_POST(self):
        response = self.client.post(self.login_url, {
            'email': 'jeremy@etna.net',
            'password': '123456'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

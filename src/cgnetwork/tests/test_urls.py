from django.test import SimpleTestCase
from django.urls import reverse, resolve
from cgnetwork.views import (
    register,
    home
    )


class TestUrls(SimpleTestCase):

    def test_register_url_is_resolved(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, register)

    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)

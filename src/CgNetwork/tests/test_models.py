from django.test import TestCase
from CgNetwork.models import CustomUser
from django.utils import timezone


class TestCustomUserModel(TestCase):

    def setUp(self):
        self.random_user = CustomUser.objects.create(
            email='jeremy@etna.net',
            register_date=timezone.now,
            is_active=True,
            user_role='artist',
            country='France',
            state='',
            city='Paris',
            zip_code='75007',
            street_name='Avenue de saxe',
            street_number='43',
            phone_number='0160224541'
        )

    def test_artist_creation(self):
        self.assertEqual(self.random_user.state, "aaaa")

from django.test import TestCase
from myapp.models import MyModel


class MyModelTestCase(TestCase):
    def setUp(self):
        MyModel.objects.create(name="test")

    def test_my_model(self):
        my_model = MyModel.objects.get(name="test")
        self.assertEqual(my_model.name, "test")

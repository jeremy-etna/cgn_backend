import unittest
from unittest.mock import Mock
from django.test import TestCase
from users.data_manager import (
    get_profile_data,
    get_artist_profile_data,
    get_company_profile_data,
    convert_objects_to_dict,
    get_templates,
    get_artist_card_data,
)


class TestGetProfileData(TestCase):
    def test_get_profile_data(self):
        # Mock the models and their objects
        mock_model = Mock()
        mock_model.objects.get.return_value = "mock_value"
        models = [(mock_model, "mock_key")]

        user_id = 1

        expected = {"mock_key": "mock_value"}
        result = get_profile_data(user_id, models)

        self.assertEqual(expected, result)


class TestGetArtistProfileData(TestCase):
    def test_get_artist_profile_data(self):
        # Mock the get_profile_data function
        get_profile_data = Mock()
        get_profile_data.return_value = "mock_value"

        user_id = 1

        expected = "mock_value"
        result = get_artist_profile_data(user_id)

        self.assertEqual(expected, result)


class TestGetCompanyProfileData(TestCase):
    def test_get_company_profile_data(self):
        # Mock the get_profile_data function
        get_profile_data = Mock()
        get_profile_data.return_value = "mock_value"

        user_id = 1

        expected = "mock_value"
        result = get_company_profile_data(user_id)

        self.assertEqual(expected, result)


class TestConvertObjectsToDict(TestCase):
    def test_convert_objects_to_dict(self):
        mock_obj = Mock()
        mock_obj.__dict__ = {"id": 1, "user": 1, "field1": "value1", "field2": "value2"}
        mock_obj._meta.fields = [
            Mock(name="id"),
            Mock(name="user"),
            Mock(name="field1"),
            Mock(name="field2"),
        ]

        context = {"mock_key": mock_obj}

        expected = {"mock_key": {"field1": "value1", "field2": "value2"}}
        result = convert_objects_to_dict(context)

        self.assertEqual(expected, result)


class TestGetTemplates(unittest.TestCase):
    def test_get_templates(self):
        role = "role"
        components = ["component1", "component2"]

        expected = {
            "component1": "role/components/component1.html",
            "component2": "role/components/component2.html",
        }
        result = get_templates(role, components)

        self.assertEqual(expected, result)


class TestGetArtistCardData(TestCase):
    def test_get_artist_card_data(self):
        # Mock the user, models, and their objects
        mock_user = Mock(id=1)
        mock_model = Mock()
        mock_model.objects.get.return_value = "mock_value"
        models = [(mock_model, "mock_key")]

        users = [mock_user]

        expected = {mock_user: {"mock_key": "mock_value"}}
        result = get_artist_card_data(users)

        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()

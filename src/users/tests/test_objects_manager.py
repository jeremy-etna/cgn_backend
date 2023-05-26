import os
from django.test import TestCase

from django.conf import settings

from users.models.common import CustomUser
from users.models.artist import ArtistIdentity

from cgnetwork.constants.models import (
    Role,
)

from users.services.objects_manager import (
    get_objects_from_models,
    get_all_objects_from_models,
    remove_elements_by_keys_recursive,
    get_templates,
    get_template,
    remove_pattern_dict_keys,
)


class ObjectsManagerTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(
            id=1000, email="test@example.com", password="123456789", role=Role.ARTIST
        )
        self.artist = ArtistIdentity.objects.last()

        self.artist.title = "Oceanographer"
        self.artist.first_name = "Alexander"
        self.artist.last_name = "Braun"
        self.artist.description = "description"
        self.artist.user = self.user
        self.artist.save()

    def test_get_objects_from_models(self):
        models = [ArtistIdentity]
        result = get_objects_from_models(models, self.user.id)

        self.assertEqual(len(result), 1)
        self.assertEqual(result["artistidentity"]["user"], 1000)
        self.assertEqual(result["artistidentity"]["title"], "Oceanographer")
        self.assertEqual(result["artistidentity"]["first_name"], "Alexander")
        self.assertEqual(result["artistidentity"]["last_name"], "Braun")
        self.assertEqual(result["artistidentity"]["description"], "description")

    def test_get_all_objects_from_models(self):
        models = [ArtistIdentity]
        artist_identity_instances_number = ArtistIdentity.objects.count()
        result = get_all_objects_from_models(models)

        self.assertEqual(len(result), artist_identity_instances_number)


class RemoveElementsTestCase(TestCase):
    def test_remove_elements_by_keys_recursive_single_key(self):
        dictionary = {
            "key1": "value1",
            "key2": "value2",
            "key3": {
                "nested_key1": "nested_value1",
                "nested_key2": "nested_value2",
            },
            "key4": ["value3", "value4"],
        }
        keys_to_remove = "key2"
        result = remove_elements_by_keys_recursive(dictionary, keys_to_remove)
        expected_result = {
            "key1": "value1",
            "key3": {
                "nested_key1": "nested_value1",
                "nested_key2": "nested_value2",
            },
            "key4": ["value3", "value4"],
        }

        self.assertDictEqual(result, expected_result)

    def test_remove_elements_by_keys_recursive_multiple_keys(self):
        dictionary = {
            "key1": "value1",
            "key2": "value2",
            "key3": {
                "nested_key1": "nested_value1",
                "nested_key2": "nested_value2",
            },
            "key4": ["value3", "value4"],
        }
        keys_to_remove = ["key2", "nested_key1"]
        result = remove_elements_by_keys_recursive(dictionary, keys_to_remove)
        expected_result = {
            "key1": "value1",
            "key3": {
                "nested_key2": "nested_value2",
            },
            "key4": ["value3", "value4"],
        }

        self.assertDictEqual(result, expected_result)

    def test_remove_elements_by_keys_recursive_no_keys_to_remove(self):
        dictionary = {
            "key1": "value1",
            "key2": "value2",
            "key3": {
                "nested_key1": "nested_value1",
                "nested_key2": "nested_value2",
            },
            "key4": ["value3", "value4"],
        }
        keys_to_remove = []
        result = remove_elements_by_keys_recursive(dictionary, keys_to_remove)

        self.assertDictEqual(result, dictionary)


class GetTemplatesTestCase(TestCase):
    def test_get_templates(self):
        role = "artist"
        components = ["header", "footer", "sidebar"]
        result = get_templates(role, components)
        expected_result = {
            "header": "artist/components/header.html",
            "footer": "artist/components/footer.html",
            "sidebar": "artist/components/sidebar.html",
        }

        self.assertDictEqual(result, expected_result)

    def test_get_templates_empty_components(self):
        role = "admin"
        components = []
        result = get_templates(role, components)

        self.assertDictEqual(result, {})


class GetTemplateTestCase(TestCase):
    def test_get_template(self):
        app = "users"
        role = "artist"
        component = "header"
        result = get_template(app, role, component)
        expected_result = os.path.join(
            settings.BASE_DIR, "users", "templates", "artist", "components", "header"
        )

        self.assertEqual(result, expected_result)

    def test_get_template_different_app(self):
        app = "cgnetwork"
        role = "company"
        component = "footer"
        result = get_template(app, role, component)
        expected_result = os.path.join(
            settings.BASE_DIR,
            "cgnetwork",
            "templates",
            "company",
            "components",
            "footer",
        )

        self.assertEqual(result, expected_result)


class RemovePatternDictKeysTestCase(TestCase):
    def test_remove_pattern_dict_keys(self):
        dictionary = {
            "key_1": "value1",
            "key_2": "value2",
            "key_3": "value3",
        }
        pattern = "key_"
        result = remove_pattern_dict_keys(dictionary, pattern)
        expected_result = {
            "1": "value1",
            "2": "value2",
            "3": "value3",
        }

        self.assertDictEqual(result, expected_result)

    def test_remove_pattern_dict_keys_no_match(self):
        dictionary = {
            "key1": "value1",
            "key2": "value2",
            "key3": "value3",
        }
        pattern = "pattern_"
        result = remove_pattern_dict_keys(dictionary, pattern)

        self.assertDictEqual(result, dictionary)

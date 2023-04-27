from django.test import TestCase
from unittest.mock import patch
from cgnetwork.settings import BASE_DIR
from cgnetwork.context_OLD import Context

class TestContext(TestCase):

    def setUp(self):
        self.ctx = Context()
        self.components = ['header', 'footer']

    @patch('os.path.exists')
    def test_check_template_exists(self, mock_exists):
        mock_exists.return_value = True
        result = self.ctx._check_template_exists('app_name', 'template_path')
        self.assertTrue(result)

    @patch('os.path.exists')
    def test_check_template_not_exists(self, mock_exists):
        mock_exists.return_value = False
        result = self.ctx._check_template_exists('app_name', 'template_path')
        self.assertFalse(result)

    def test_modify_template_root(self):
        modified_template = self.ctx._modify_template_root('app_name', 'role/components/header.html')
        expected_path = os.path.join(BASE_DIR, 'app_name', 'templates', 'common/components/header.html')
        self.assertEqual(modified_template, expected_path)

    def test_resolve_template_from_component(self):
        template_path = self.ctx._resolve_template_from_component('header')
        self.assertEqual(template_path, 'common/components/header.html')

    @patch('os.path.exists')
    def test_get_templates(self, mock_exists):
        mock_exists.side_effect = [True, True]
        templates = self.ctx.get_templates('app_name', self.components)
        expected_templates = {
            'header': 'common/components/header.html',
            'footer': 'common/components/footer.html'
        }
        self.assertDictEqual(templates, expected_templates)

    def test_resolve_model_form_from_component_name(self):
        forms = {'Common, HeaderForm': 'header_form', 'Common, FooterForm': 'footer_form'}
        form = self.ctx._resolve_model_form_from_component_name('header', forms)
        self.assertEqual(form, 'header_form')

    def test_resolve_model_form_from_component_name_not_found(self):
        forms = {'Common, HeaderForm': 'header_form'}
        with self.assertRaises(ValueError):
            self.ctx._resolve_model_form_from_component_name('footer', forms)

    def test_get_forms(self):
        forms = {'Common, HeaderForm': 'header_form', 'Common, FooterForm': 'footer_form'}
        result = self.ctx.get_forms(self.components, forms)
        expected_forms = {
            'header': 'header_form',
            'footer': 'footer_form'
        }
        self.assertDictEqual(result, expected_forms)

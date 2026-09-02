from django.test import Client, TestCase


class PublicPagesTests(TestCase):
    def setUp(self):
        self.client = Client(HTTP_HOST='localhost')

    def test_home_page_is_available(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Gestión de Inmuebles')

    def test_explicit_404_page_is_custom(self):
        response = self.client.get('/404/')

        self.assertEqual(response.status_code, 404)
        self.assertContains(response, 'Este espacio', status_code=404)

    def test_unknown_url_uses_custom_404_handler(self):
        response = self.client.get('/ruta-inexistente/')

        self.assertEqual(response.status_code, 404)
        self.assertContains(response, 'Este espacio', status_code=404)

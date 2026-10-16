from django.test import Client, TestCase
from django.urls import resolve, reverse
from rest_framework.test import APIClient


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


class ApiCrudTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_all_resources_expose_complete_crud_routes(self):
        resources = [
            'paises', 'regiones', 'provincias', 'comunas', 'direcciones',
            'inmobiliarias', 'tipos-inmueble', 'tipos-operacion',
            'estados-inmueble', 'caracteristicas', 'propietarios', 'agentes',
            'clientes', 'inmuebles', 'inmuebles-caracteristicas', 'visitas',
            'historial-estados', 'operaciones',
        ]
        list_actions = {'get': 'list', 'post': 'create'}
        detail_actions = {
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy',
        }

        for resource in resources:
            with self.subTest(resource=resource):
                list_view = resolve(f'/inmuebles_app/{resource}/').func
                detail_view = resolve(f'/inmuebles_app/{resource}/1/').func
                self.assertEqual(list_view.actions, list_actions)
                self.assertEqual(detail_view.actions, detail_actions)

    def test_tipo_inmueble_can_be_created_read_updated_and_deleted(self):
        url = reverse('tipoinmueble-list')
        response = self.client.post(url, {'tipo': 'Casa'}, format='json')

        self.assertEqual(response.status_code, 201)
        detail_url = reverse('tipoinmueble-detail', args=[response.data['id']])

        self.assertEqual(self.client.get(detail_url).status_code, 200)
        response = self.client.put(detail_url, {'tipo': 'Casa remodelada'}, format='json')
        self.assertEqual(response.status_code, 200)
        response = self.client.patch(detail_url, {'tipo': 'Casa nueva'}, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['tipo'], 'Casa nueva')
        self.assertEqual(self.client.delete(detail_url).status_code, 204)

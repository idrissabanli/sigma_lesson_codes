import base64
from django.test import TestCase, Client
from django.urls import reverse_lazy
from core.forms import ContactForm
from core.models import Contact


class ContactAPIViewTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.url = reverse_lazy('recipes')
        client = Client()
        cls.get_res = client.get(cls.url)
        headers = {
            'HTTP_AUTHORIZATION': 'Basic ' + base64.b64encode(b'idris:i4383930S')
        }
        cls.valid_data = {
            'title': 'Idris',
            'short_description': 'idris@gmail.com',
            'description': 'askndfkasdnf',
            'image': 'image.png',
            'cover_image': 'image.png',
            'tags': 1,
            'category': 1,
        }
        cls.post_res = client.post(cls.url, data=cls.valid_data, content_type='application/json', **headers)

    def test_url(self):
        self.assertEqual(self.url, '/api/recipes/')

    def test_get_request_status_code(self):
        self.assertEqual(self.get_res.status_code, 200)

    def test_get_request_response_content_type(self):
        self.assertEqual(self.get_res['content-type'], 'application/json')

    def test_get_request_response_data(self):
        self.assertIsInstance(self.get_res.json(), list)

    def test_post_request_status_code(self):
        print(self.post_res.json())
        self.assertEqual(self.post_res.status_code, 201)


    @classmethod
    def tearDownClass(cls):
        pass
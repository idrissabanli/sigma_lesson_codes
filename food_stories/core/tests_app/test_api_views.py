import os
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from django.urls import reverse_lazy
from core.forms import ContactForm
from core.models import Contact
from stories.models import Category, Tag
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()


class ContactAPIViewTest(TestCase):

    @classmethod
    def setUpClass(cls):
        user = User.objects.create_user(username='john', email='js@js.com', password='js.sj')
        cls.url = reverse_lazy('recipes')
        refresh = RefreshToken.for_user(user)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        cls.get_res = client.get(cls.url)
        file_path = os.path.join(settings.MEDIA_ROOT, 'recipes/1_Alz3yyO.png')
        category = Category.objects.create(title='title', image='image.png')
        tag = Tag.objects.create(title='title')
        cls.valid_data = {
            'title': 'Idris',
            'short_description': 'idris@gmail.com',
            'description': 'askndfkasdnf',
            'image': (open(file_path, 'rb'),),
            'cover_image': (open(file_path, 'rb'),),
            'tags': tag.id,
            'category': category.id
        }
        cls.post_res = client.post(cls.url, cls.valid_data)

    def test_url(self):
        self.assertEqual(self.url, '/api/recipes/')

    def test_get_request_status_code(self):
        self.assertEqual(self.get_res.status_code, 200)

    def test_get_request_response_content_type(self):
        self.assertEqual(self.get_res['content-type'], 'application/json')

    def test_get_request_response_data(self):
        self.assertIsInstance(self.get_res.json(), list)

    def test_post_request_status_code(self):
        self.assertEqual(self.post_res.status_code, 201)


    @classmethod
    def tearDownClass(cls):
        pass
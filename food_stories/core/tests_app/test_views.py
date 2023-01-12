from django.test import TestCase, Client
from django.urls import reverse_lazy
from core.forms import ContactForm
from core.models import Contact


class ContactViewTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.url = reverse_lazy('core:contact')
        client = Client()
        cls.get_res = client.get(cls.url)
        cls.valid_data = {
            'name': 'Idris',
            'email': 'idris@gmail.com',
            'subject': 'askndfkasdnf',
            'message': 'slkdfnskldnfkndf',
        }

        cls.invalid_data = {
            'name': 'sdjkfn',
            'email': 'idris'
        }
        cls.get_post_valid = client.post(cls.url, data=cls.valid_data)
        cls.get_post_invalid = client.post(cls.url, data=cls.invalid_data)

    def test_url(self):
        self.assertEqual(self.url, '/az/contact/')

    def test_get_request_status_code(self):
        self.assertEqual(self.get_res.status_code, 200)

    def test_get_request_template(self):
        self.assertTemplateUsed(self.get_res, 'contact.html')

    def test_get_request_context(self):
        self.assertIsInstance(self.get_res.context['form'], ContactForm)
    
    def test_post_request_redirect(self):
        self.assertRedirects(self.get_post_valid, reverse_lazy('core:home'), 302, 200)

    def test_post_request_creation(self):
        contact = Contact.objects.first()
        self.assertEqual(contact.name, self.valid_data['name'])

    def test_post_request_errors(self):
        form = self.get_post_invalid.context['form']
        self.assertFalse(form.is_valid())
        self.assertIn('Keçərli e-poçt ünvanı daxil edin.', form.errors['email'])
        self.assertIn('Bu sahə tələb edilir.', form.errors['subject'])
        self.assertIn('Bu sahə tələb edilir.', form.errors['message'])


    @classmethod
    def tearDownClass(cls):
        pass
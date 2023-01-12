from django.test import TestCase
from core.forms import ContactForm


class ContactFormTest(TestCase):

    @classmethod
    def setUpClass(cls):
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
        
    def test_valid_data_validation(self):
        form = ContactForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_invalid_data_validation(self):
        form = ContactForm(data=self.invalid_data)
        self.assertFalse(form.is_valid())

    def test_invalid_data_error_messages(self):
        form = ContactForm(data=self.invalid_data)
        self.assertIn('Keçərli e-poçt ünvanı daxil edin.', form.errors['email'])
        self.assertIn('Bu sahə tələb edilir.', form.errors['subject'])
        self.assertIn('Bu sahə tələb edilir.', form.errors['message'])

    @classmethod
    def tearDownClass(cls):
        pass
    
    
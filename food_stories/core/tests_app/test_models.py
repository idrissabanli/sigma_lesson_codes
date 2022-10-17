from django.test import TestCase
from core.models import Contact


class ContactModelTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = {
            'name': 'Idris',
            'email': 'idris@gmail.com',
            'subject': 'Something',
            'message': 'message'
        }
        cls.contact = Contact.objects.create(**cls.data)

    def test_create_method(self):
        contact = Contact.objects.first()
        self.assertEqual(self.contact, contact)

    def test_str_method(self):
        contact = Contact.objects.first()
        self.assertEqual(str(self.contact), f"{self.data['name']} Subject: {self.data['subject']}")
    
    @classmethod
    def tearDownClass(cls):
        pass
        
    

    
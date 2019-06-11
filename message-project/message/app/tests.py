from django.test import Client
from django.test import TestCase


class SimpleTest(TestCase):
    def setUp(self):
        self.c = Client()

    def test_msg(self):
        response = self.c.get('/msg/')
        self.assertEqual(response.status_code, 200)

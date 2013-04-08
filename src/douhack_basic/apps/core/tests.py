from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse


class CoreTest(TestCase):
    """
    Test core app 
    """

    def test_home_page(self):
        """
        - home page must open with status 200
        - user must be able to register
        - user must be able to confirm he will take part
        """
        c = Client()
        response = c.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

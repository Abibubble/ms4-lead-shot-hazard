from django.test import TestCase

from django.shortcuts import reverse
from django.contrib.auth.models import User, AnonymousUser

from checkout.models import Order

class TestViews(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            username="testuser", email="test@test.com", password="te12345st")

    def test_checkout_page(self):
        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/products/")

    def test_cache_checkout_data_get(self):
        response = self.client.get('/checkout/cache_checkout_data/')
        self.assertEqual(response.status_code, 405)

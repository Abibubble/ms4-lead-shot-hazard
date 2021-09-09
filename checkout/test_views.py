from django.test import TestCase

from django.shortcuts import reverse
from django.contrib.auth.models import User


class TestCheckoutViews(TestCase):
    """
    Test that the checkout page and checkout cache work as expected
    """

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            username="testuser", email="test@test.com", password="te12345st")

    # Test that the checkout page loads and redirects as expected
    def test_the_checkout_page(self):
        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/products/")

    # Test that the cache_checkout_data function responds correctly
    def test_cache_checkout_data(self):
        response = self.client.get('/checkout/cache_checkout_data/')
        self.assertEqual(response.status_code, 405)

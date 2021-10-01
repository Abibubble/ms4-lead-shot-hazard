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

    # Test that the checkout page URL exists
    def test_the_checkout_page_url_exists(self):
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 302)

    # Test that the checkout page is accessible via name
    def test_the_checkout_url_is_accessible_by_name(self):
        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 302)

    # Test that the checkout page redirects correctly
    def test_checkout_view_uses_correct_template(self):
        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/products/")

    # Test that the cache_checkout_data function responds correctly
    def test_cache_checkout_data(self):
        response = self.client.get('/checkout/cache_checkout_data/')
        self.assertEqual(response.status_code, 405)

from django.test import TestCase

from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages

from products.models import Product
from .models import Order


class TestCheckoutViews(TestCase):
    """
    Test that the checkout page and checkout cache work as expected
    """

    @classmethod
    def setUpTestData(self):
        User.objects.create_user(
            username='testuser', email='test@test.com', password='te12345st')

    # Test that the cache_checkout_data function responds correctly
    def test_cache_checkout_data(self):
        response = self.client.get('/checkout/cache_checkout_data/')
        self.assertEqual(response.status_code, 405)

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
        self.assertRedirects(response, '/products/')

    # Test that an error message is shown when nothing is in the shopping bag
    def test_nothing_in_bag_error(self):
        response = self.client.get('/checkout/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].tags, 'error')
        self.assertEqual(
            str(messages[0]), "There's nothing in your bag at the moment.")

    # Test that the bag can be retrieved from the session
    # def test_bag_from_session(self):
    #     session = self.client.session
    #     bag = {'14': 1, '11': 1}
    #     session['bag'] = bag
    #     session.save()

    # # Test that an error message is shown when Stripe key is missing
    # def test_no_stripe_key_error(self):
    #     stripe_public_key = 'somekey'
    #     del stripe_public_key
    #     response = self.client.get('/checkout/')
    #     messages = list(get_messages(response.wsgi_request))
    #     self.assertEqual(len(messages), 1)
    #     self.assertEqual(messages[0].tags, 'error')
    #     self.assertEqual(
    #         str(messages[0]), 'Stripe public key is missing.')

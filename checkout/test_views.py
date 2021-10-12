"""
This module tests the views in the checkout app
"""

from django.test import TestCase

from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.conf import settings

from products.models import Product
from .models import Order


class TestCheckoutViews(TestCase):
    """
    Test that the checkout page and checkout cache work as expected
    """

    fixtures = [
        'categories.json',
        'products.json',
    ]

    @classmethod
    def setUpTestData(self):
        User.objects.create_user(
            username='testuser', email='test@test.com', password='te12345st')

    def test_cache_checkout_data(self):
        """
        Test that the cache_checkout_data function responds correctly
        """
        response = self.client.get('/checkout/cache_checkout_data/')
        self.assertEqual(response.status_code, 405)

    def test_the_checkout_page_url_exists(self):
        """
        Test that the checkout page URL exists
        """
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 302)

    def test_the_checkout_url_is_accessible_by_name(self):
        """
        Test that the checkout page is accessible via name
        """
        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 302)

    def test_checkout_view_uses_correct_template(self):
        """
        Test that the checkout page redirects correctly
        """
        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/products/')

    def test_nothing_in_bag_error(self):
        """
        Test that an error message is shown when nothing is in the shopping bag
        """
        response = self.client.get('/checkout/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].tags, 'error')
        self.assertEqual(
            str(messages[0]), "There's nothing in your bag at the moment.")

    # def test_bag_from_session(self):
    #     """
    #     Test that the bag can be retrieved from the session
    #     """
    #     user = User.objects.create_user(
    #         username="testcheckoutuser", email="test@testcheckout.com",
    #         password="te12345st")
    #     self.client.login(
    #         username=user.username, email=user.email, password="te12345st")
    #     form_data = {
    #         'full_name': 'test user',
    #         'email': user.email,
    #         'phone_number': '09866543123',
    #         'town_or_city': 'test city',
    #         'street_address1': 'test address',
    #         'street_address2': 'test address 2',
    #         'county': 'test county',
    #         'country': 'GB',
    #         'postcode': '55555'
    #     }
    #     client_secret = 'pi_6DjAtJRwwOhT6EHb45OLEFdD_secret'
    #     session = self.client.session
    #     bag = {'14': 1, '11': 1}
    #     session['bag'] = bag
    #     self.client.post('/checkout/', form_data)

    def test_no_stripe_key_error(self):
        """
        Test that an error message is shown when Stripe key is missing
        """
        bag = {'14': 1, '11': 1}
        session = self.client.session
        session['bag'] = bag
        session.save()
        response = self.client.get(
            '/checkout/', session['bag'], stripe_public_key=None)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].tags, 'warning')
        self.assertEqual(
            str(messages[0]), 'Stripe public key is missing.')

"""
This module tests the views in the checkout app
"""

from django.test import TestCase

from django.shortcuts import reverse, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.conf import settings

import stripe

from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from products.models import Product, Category
from .models import Order, OrderLineItem
from .forms import OrderForm


class TestCheckoutViews(TestCase):
    """
    Test that the checkout page and checkout cache work as expected
    """

    fixtures = [
        'categories.json',
        'products.json',
    ]

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@test.com',
            password='te12345st'
        )

        self.admin = User.objects.create_superuser(
            username='testadmin',
            email='testadmin@test.com',
            password='te12345st'
        )

        self.category = Category.objects.create(
            name='testcategory',
            friendly_name='Test Category'
        )

        self.item = Product.objects.create(
            category=self.category,
            name='test product',
            description='testing product description',
            price=0.01,
            sku='1111',
        )

        self.quantity = 1

        self.empty_bag = {}

        self.filled_bag = {'14': 1, '11': 1}

        self.bad_bag = {'200': 1}

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

    def test_no_stripe_key_error(self):
        """
        Test that an error message is shown when Stripe key is missing
        """
        bag = {'14': 1, '11': 1}
        session = self.client.session
        session['bag'] = bag
        session.save()
        settings.STRIPE_PUBLIC_KEY = ''
        response = self.client.get('/checkout/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].tags, 'warning')
        self.assertEqual(
            str(messages[0]), 'Stripe public key is missing.')

    def test_get_checkout_view(self):
        """
        Test that the checkout view works with items in the shopping bag
        """
        session = self.client.session
        session['bag'] = self.filled_bag
        session.save()
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 200)

    def test_checkout_autofill_details_if_logged_in(self):
        """
        Check if user is authenticated and logged in,
        and if they are, autofill the form with their details
        """
        session = self.client.session
        session['bag'] = self.filled_bag
        session.save()
        self.client.force_login(self.user)
        response = self.client.get('/checkout/')
        user_profile = get_object_or_404(UserProfile, user=self.user)
        user_profile_form = UserProfileForm({
            'default_phone_number': '09876543212',
            'default_street_address11': 'test',
            'default_street_address2': 'test',
            'default_town_or_city': 'test',
            'default_county': 'test',
            'default_postcode': 'test',
            'default_country': 'GB'
        },
            instance=user_profile
        )

        self.assertTrue(user_profile_form.is_valid())
        user_profile_form.save()
        order_form = response.context['order_form']
        self.assertGreater(len(order_form.initial), 1)

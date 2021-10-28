from django.test import TestCase, Client

from django.shortcuts import reverse
from django.contrib.messages import get_messages
from django.contrib.auth.models import User

from checkout.models import Order


class TestProfileViews(TestCase):
    """
    Test that the user profile page displays when logged in
    """

    def setUp(self):
        self.client = Client()
        User.objects.create_user(
            username="testuser", email="test@test.com", password="te12345st")

    def test_the_profiles_page_url_exists(self):
        """
        Test that the profiles page URL exists
        """
        self.client.login(
            username="testuser", email="test@test.com", password="te12345st")
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)

    def test_the_profiles_url_is_accessible_by_name(self):
        """
        Test that the profiles page is accessible via name
        """
        self.client.login(
            username="testuser", email="test@test.com", password="te12345st")
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)

    def test_logged_in_user_profile_page(self):
        """
        Test that a logged in user can access their
        profile page, and a logged out user can't
        """
        self.client.login(
            username="testuser", email="test@test.com", password="te12345st")
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, template_name="profiles/profile.html")

    def test_profile_gets_saved_for_valid_form(self):
        """
        Test that the user's profile data is saved if the form is valid
        """
        user = User.objects.create_user(
            username="testprofileuser", email="test@testprofile.com",
            password="te12345st")
        self.client.login(
            username=user.username, email=user.email, password="te12345st")
        user_data = {
            'default_phone_number': 'tester',
            'default_street_address1': 'test',
            'default_town_or_city': 'test',
            'default_postcode': '55555',
            'default_county': 'test',
            'default_country': 'GB'
        }
        self.client.post('/profile/', user_data)
        response = self.client.post('/profile/', user_data)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].tags, 'success')
        self.assertEqual(
            str(messages[0]), 'Profile updated successfully!')

    def test_order_history_displays_when_requested(self):
        """
        Test that the order history is shown in full when user is logged in
        """
        self.client.login(
            username="testuser", email="test@test.com", password="te12345st")
        Order.objects.create(
            order_number='1EC'
        )
        order_number = '1EC'
        response = self.client.get(
            f'/profile/order_history/{order_number}/')
        self.assertTemplateUsed(
            response, template_name="checkout/checkout_success.html")

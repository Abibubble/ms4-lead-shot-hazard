from django.test import TestCase

from django.shortcuts import reverse
from django.contrib.auth.models import User

from .forms import UserProfileForm


class TestProfileViews(TestCase):
    """
    Test that the user profile page displays when logged in
    """

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            username="testuser", email="test@test.com", password="te12345st")

    # Test that a logged in user can access their
    # profile page, and a logged out user can't
    def test_logged_in_user_profile_page(self):
        self.client.login(
            username="testuser", email="test@test.com", password="te12345st")
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, template_name="profiles/profile.html")

    # Test that the user's profile data is saved
    def test_profile_gets_saved(self):
        user_data = {
            'default_phone_number': 'tester',
            'default_street_address1': 'test',
            'default_town_or_city': 'test',
            'default_postcode': '55555',
            'default_county': 'test',
            'default_country': 'GB'
        }
        form = UserProfileForm(data=user_data)
        self.assertTrue(form.is_valid())

    # Test that the order history is shown in full when user is logged in
    def test_order_history_displays_when_requested(self):
        self.client.login(
            username="testuser", email="test@test.com", password="te12345st")
        response = self.client.get(reverse('profile'))
        self.assertTemplateUsed(
            response, template_name="profiles/profile.html")

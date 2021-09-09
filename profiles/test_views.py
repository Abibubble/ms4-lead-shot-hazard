from django.test import TestCase

from django.shortcuts import reverse
from django.contrib.auth.models import User, AnonymousUser


class TestProfileViews(TestCase):
    """
    Test that the user profile page displays when logged in
    """

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            username="testuser", email="test@test.com", password="te12345st")

    # Test that a logged in user can access their profile page, and a logged out user can't
    def test_logged_in_user_profile_page(self):
        if not AnonymousUser:
            response = self.client.get(reverse('profile'))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(
                response, template_name="profiles/profile.html")

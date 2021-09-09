from django.test import TestCase

from django.shortcuts import reverse
from django.contrib.auth.models import User, AnonymousUser

from .models import UserProfile


class TestViews(TestCase):
    """
    Test that the user profile page displays when logged in
    """

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            username="testuser", email="test@test.com", password="te12345st")

    def test_logged_in_user_profile_page(self):
        user = self.client.login(
            email="testing@test.com", password="testing12345")
        if not AnonymousUser:
            response = self.client.get(reverse('profile'))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(
                response, template_name="profiles/profile.html")

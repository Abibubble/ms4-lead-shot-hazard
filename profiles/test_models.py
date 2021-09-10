from django.test import TestCase
from django.contrib.auth.models import User


class UserProfileTest(TestCase):
    """
    Test that the user profile works as expected
    """

    @classmethod
    def setUpTestData(self):
        self.user = User.objects.create(username='testuser')
        self.user.set_password('te12345st')
        self.user.save()

    # Test retrieving the user profile
    def test_getting_user_profile(self):
        self.client.login(username='testuser', password='te12345st')
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

    # Test string method
    def test_string_method_returns_username(self):
        self.assertEqual(str(self.user.username), "testuser")

    def test_user_string(self):
        self.assertEqual(self.user.__str__(),  self.user.username)

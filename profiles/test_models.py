from django.test import TestCase, Client
from django.contrib.auth.models import User


class UserProfileTest(TestCase):
    """
    Test that the user profile works as expected
    """

    @classmethod
    def setUpTestData(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', email='test@test.com', password='te12345st')
        self.client.login(
            username='testuser', email='test@test.com', password='te12345st')

    def test_getting_user_profile(self):
        """
        Test retrieving the user profile
        """
        self.client.login(username='testuser', password='te12345st')
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

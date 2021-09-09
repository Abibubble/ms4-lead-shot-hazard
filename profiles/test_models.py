from django.test import TestCase
from django.contrib.auth.models import User


class UserProfileTest(TestCase):
    """
    Test that the user profile works as expected
    """

    # Test retrieving the user profile
    def test_getting_user_profile(self):
        user = User.objects.create(username='testuser')
        user.set_password('te12345st')
        user.save()
        self.client.login(username='testuser', password='te12345st')
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

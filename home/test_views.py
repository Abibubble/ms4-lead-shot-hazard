from django.test import TestCase

from django.shortcuts import reverse


class TestHomeViews(TestCase):
    """
    Test that the home page displays correctly
    """

    # Test that the homepage returns a 200 response
    def test_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name="home/index.html")

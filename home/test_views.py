from django.test import TestCase

from django.shortcuts import reverse


class TestHomeViews(TestCase):
    """
    Test that the home page displays correctly
    """

    # Test that the home page URL exists
    def test_the_home_page_url_exists(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    # Test that the home page is accessible via name
    def test_the_home_url_is_accessible_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    # Test that the home page uses the correct template
    def test_home_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, template_name="home/index.html")

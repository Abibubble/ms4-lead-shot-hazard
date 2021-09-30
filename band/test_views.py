from django.test import TestCase

from django.shortcuts import reverse


class TestBandViews(TestCase):
    """
    Test that the contact us and upcoming gigs pages work as expected
    """

    # Test that the contact us page loads and redirects as expected
    def test_the_contact_us_page(self):
        response = self.client.get(reverse('view_contact'))
        self.assertEqual(response.status_code, 200)

    # Test that the upcoming gigs page loads and redirects as expected
    def test_upcoming_gigs_page(self):
        response = self.client.get(reverse('view_gigs'))
        self.assertEqual(response.status_code, 200)

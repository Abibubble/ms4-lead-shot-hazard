from django.test import TestCase

from django.shortcuts import reverse


class TestBandViews(TestCase):
    """
    Test that the contact us and upcoming gigs pages work as expected
    """

    @classmethod
    def setUpTestData(cls):
        current_event = {
            'venue_name': 'test venue',
            'band_line_up': ['test band'],
            'year': 2021,
            'month': 'December',
            'day': 25,
            'weekday': 'Monday',
            'time': '14:00',
            'location': 'Leicester, UK',
            'songkick_link': 'https://www.google.com'
        }

    # Test that the contact us page loads and redirects as expected
    def test_the_contact_us_page(self):
        response = self.client.get(reverse('view_contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, template_name="band/contact.html")

    # Test that the upcoming gigs page loads and redirects as expected
    def test_upcoming_gigs_page(self):
        response = self.client.get(reverse('view_gigs'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, template_name="band/gigs.html")

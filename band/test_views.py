from django.test import TestCase

from django.shortcuts import reverse


class TestBandViews(TestCase):  # pragma: no cover
    """
    Test that the contact us and upcoming gigs pages work as expected
    """

    def test_the_contact_us_page_url_exists(self):
        """
        Test that the contact us page URL exists
        """
        response = self.client.get('/band/contact-us/')
        self.assertEqual(response.status_code, 200)

    def test_the_contact_us_url_is_accessible_by_name(self):
        """
        Test that the contact us page is accessible via name
        """
        response = self.client.get(reverse('view_contact'))
        self.assertEqual(response.status_code, 200)

    def test_contact_us_view_uses_correct_template(self):
        """
        Test that the contact us page uses the correct template
        """
        response = self.client.get(reverse('view_contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, template_name="band/contact.html")

    def test_the_upcoming_gigs_page_url_exists(self):
        """
        Test that the upcoming gigs page URL exists
        """
        response = self.client.get('/band/gigs/')
        self.assertEqual(response.status_code, 200)

    def test_the_upcoming_gigs_url_is_accessible_by_name(self):
        """
        Test that the upcoming gigs page is accessible via name
        """
        response = self.client.get(reverse('view_gigs'))
        self.assertEqual(response.status_code, 200)

    def test_upcoming_gigs_view_uses_correct_template(self):
        """
        Test that the upcoming gigs page uses the correct template
        """
        response = self.client.get(reverse('view_gigs'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, template_name="band/gigs.html")

from django.test import TestCase

from django.shortcuts import reverse


class TestBagViews(TestCase):
    """
    Test that the shopping bag works as expected
    """

    def test_view_bag(self):
        response = self.client.get(reverse('view_bag'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, template_name="bag/bag.html")

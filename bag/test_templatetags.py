from django.test import TestCase

from .templatetags.bag_tools import calc_subtotal


class TestTemplateTags(TestCase):
    """
    Test template tag calc_subtotal function
    calculates the subtotal for each item correctly
    """

    def test_calc_subtotal_works(self):
        self.assertEqual(calc_subtotal(10, 5), 50)
        self.assertEqual(calc_subtotal(5, 2), 10)
        self.assertNotEqual(calc_subtotal(5, 2), 12)

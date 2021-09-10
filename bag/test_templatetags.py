from django.test import TestCase

from .templatetags.bag_tools import calc_subtotal


class TestTemplateTags(TestCase):
    """
    Test teplate tag function works as expected
    """

    def test_calc_subtotal_works(self):
        self.assertEqual(calc_subtotal(10, 5), 50)
        self.assertEqual(calc_subtotal(5, 2), 10)

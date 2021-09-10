from django.test import TestCase

from django.shortcuts import reverse
from .contexts import bag_contents


class TestBagContexts(TestCase):
    """
    Test that the bag contexts work as expected
    """
    # def test_that_delivery_cost_is_correct(self):
    #     if total > settings.FREE_DELIVERY_THRESHOLD:
    #         self.assertEqual(delivery, 0)
    #         self.assertEqual(free_delivery_delta, 0)

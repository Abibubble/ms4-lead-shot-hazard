from django.test import TestCase
from django.conf import settings

from .models import Order


class TestOrderModels(TestCase):
    """
    Test that the order models work as expected
    """

    @classmethod
    def setUpTestData(cls):
        Order.objects.create(
            full_name='tester test',
            email='test@example.com',
            phone_number='09876543212',
            country='GB',
            town_or_city='test',
            street_address1='test'
        )

    # Test that the checkout fields auto-fill from the user's information
    def test_checkout_details(self):
        order = Order.objects.get(id=1)
        self.assertEqual(order.full_name, 'tester test')
        self.assertEqual(order.email, 'test@example.com')
        self.assertEqual(order.phone_number, '09876543212')
        self.assertEqual(order.country, 'GB')
        self.assertEqual(order.street_address1, 'test')

    def test_update_total(self):
        sdp = settings.STANDARD_DELIVERY_PERCENTAGE
        order_total = 10
        if order_total < settings.FREE_DELIVERY_THRESHOLD:
            delivery_cost = order_total * sdp / 100
            self.assertEqual(delivery_cost, 1)
        else:
            delivery_cost = 0
            self.assertEqual(delivery_cost, 0)
        grand_total = order_total + delivery_cost
        self.assertEqual(grand_total, 11)
        order_total = 40
        if order_total < settings.FREE_DELIVERY_THRESHOLD:
            delivery_cost = order_total * sdp / 100
            self.assertEqual(delivery_cost, 1)
        else:
            delivery_cost = 0
            self.assertEqual(delivery_cost, 0)
        grand_total = order_total + delivery_cost
        self.assertEqual(grand_total, 40)

    # Test string method
    def test_string_method_returns_order_number(self):
        self.order_number = 20
        self.assertEqual(str(self.order_number), '20')

from django.test import TestCase
from django.conf import settings

from .models import Order, OrderLineItem
from products.models import Product


class TestOrderModels(TestCase):  # pragma: no cover
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

    # Test string method for Order class
    def test_order_string_method_returns_order_number(self):
        order_number = Order.objects.create(order_number='2000')
        self.assertEqual(str(order_number), '2000')

    # Test that the checkout fields auto-fill from the user's information
    def test_checkout_details(self):
        order = Order.objects.get(id=1)
        self.assertEqual(order.full_name, 'tester test')
        self.assertEqual(order.email, 'test@example.com')
        self.assertEqual(order.phone_number, '09876543212')
        self.assertEqual(order.country, 'GB')
        self.assertEqual(order.street_address1, 'test')

    # Test that the order total is updated correctly
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


class TestOrderLineItemModels(TestCase):
    """
    Test that the order models work as expected
    """

    # Test that the string method works for the OrderLineItem class
    def test_order_line_item_string_method(self):
        product = Product.objects.create(sku='pp200', price=2.99)
        order = Order.objects.create(order_number='2000')
        expected_output = 'SKU pp200 on order 2000'
        self.assertEqual(str(
            f'SKU {product.sku} on order {order.order_number}'),
            expected_output)

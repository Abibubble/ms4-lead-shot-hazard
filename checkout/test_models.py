from django.test import TestCase

from .models import Order


class TestOrderModels(TestCase):

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

    def test_checkout_details(self):
        order = Order.objects.get(id=1)
        self.assertEqual(order.full_name, 'tester test')
        self.assertEqual(order.email, 'test@example.com')
        self.assertEqual(order.phone_number, '09876543212')
        self.assertEqual(order.country, 'GB')
        self.assertEqual(order.street_address1, 'test')

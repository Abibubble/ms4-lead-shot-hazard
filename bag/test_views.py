"""
This module tests the views in the bag app
"""

from django.test import TestCase

from django.urls import reverse, resolve

from products.models import Product
from .views import view_bag, add_to_bag, adjust_bag, remove_from_bag


class TestBagViews(TestCase):
    """
    Test that the shopping bag works as expected
    """

    fixtures = [
        'categories.json',
        'products.json',
    ]

    def test_view_bag(self):
        """
        Test that the view_bag view responds correctly
        """
        url = reverse('view_bag')
        self.assertEqual(resolve(url).func, view_bag)
        response = self.client.get(reverse('view_bag'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, template_name="bag/bag.html")

    def test_add_to_bag(self):
        """
        Test that the add_to_bag view responds correctly
        """
        url = reverse('add_to_bag', args=['itemId'])
        self.assertEqual(resolve(url).func, add_to_bag)
        response = self.client.get(reverse('view_bag'))
        self.assertEqual(response.status_code, 200)

    def test_add_to_bag_adds_product_to_bag(self):
        """
        Test that the add_to_bag function adds products to the bag
        """
        product = Product.objects.get(pk=1)
        url = reverse('adjust_bag', args=['itemId'])
        self.assertEqual(resolve(url).func, adjust_bag)
        quantity = 1
        bag = [product.pk]
        self.assertEqual(len(bag), quantity)

    def test_adjust_bag(self):
        """
        Test that the adjust_bag view adjusts the quantity of a
        product in the bag
        """
        url = reverse('adjust_bag', args=['itemId'])
        self.assertEqual(resolve(url).func, adjust_bag)
        product = Product.objects.get(pk=1)
        quantity = 3
        bag_total = product.price * quantity
        self.assertEqual(bag_total, 30)
        quantity = 2
        bag_total += product.price * quantity
        self.assertEqual(bag_total, 50)

    def test_remove_from_bag(self):
        """
        Test that the remove_from_bag view remobves a product from the bag
        """
        url = reverse('remove_from_bag', args=['itemId'])
        self.assertEqual(resolve(url).func, remove_from_bag)

from django.test import TestCase

from django.urls import reverse, resolve

from .views import view_bag, add_to_bag, adjust_bag, remove_from_bag
from products.models import Product


class TestBagViews(TestCase):
    """
    Test that the shopping bag works as expected
    """

    fixtures = [
        'categories.json',
        'products.json',
    ]

    def test_view_bag(self):
        url = reverse('view_bag')
        self.assertEquals(resolve(url).func, view_bag)
        response = self.client.get(reverse('view_bag'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, template_name="bag/bag.html")

    def test_add_to_bag(self):
        url = reverse('add_to_bag', args=['itemId'])
        self.assertEquals(resolve(url).func, add_to_bag)

    def test_adjust_bag(self):
        url = reverse('adjust_bag', args=['itemId'])
        self.assertEquals(resolve(url).func, adjust_bag)
        product = Product.objects.get(pk=1)
        quantity = 3
        bag_total = product.price * quantity
        self.assertEqual(bag_total, 30)
        quantity = 2
        bag_total += product.price * quantity
        self.assertEqual(bag_total, 50)

    def test_remove_from_bag(self):
        url = reverse('remove_from_bag', args=['itemId'])
        self.assertEquals(resolve(url).func, remove_from_bag)

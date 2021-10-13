"""
This module tests the views in the bag app
"""

from django.test import TestCase

from django.urls import reverse, resolve
from django.shortcuts import get_object_or_404

from products.models import Product, Category
from .views import view_bag, add_to_bag, adjust_bag, remove_from_bag


class TestBagViews(TestCase):
    """
    Test that the shopping bag works as expected
    """

    fixtures = [
        'categories.json',
        'products.json',
    ]

    def setUp(self):
        self.category = Category.objects.create(
            name='testcategory',
            friendly_name='Test Category'
        )

        self.item = Product.objects.create(
            category=self.category,
            name='test product',
            description='testing product description',
            price=0.01,
            sku='1111',
        )

        self.quantity = 1

        self.empty_bag = {}

        self.filled_bag = {'14': 1, '11': 1}

        self.bad_bag = {'200': 1}

    def test_view_bag_url(self):
        """
        Test that the view_bag view responds correctly
        """
        url = reverse('view_bag')
        self.assertEqual(resolve(url).func, view_bag)
        response = self.client.get(reverse('view_bag'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, template_name="bag/bag.html")

    def test_add_to_bag_url(self):
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

    def test_adjust_bag_url(self):
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

    def test_remove_from_bag_url(self):
        """
        Test that the remove_from_bag view remobves a product from the bag
        """
        url = reverse('remove_from_bag', args=['itemId'])
        self.assertEqual(resolve(url).func, remove_from_bag)

    def test_add_to_bag_view(self):
        """
        Test that the add_to_bag view correctly adds the product to the bag
        """
        post_data = {
            'product': Product.objects.get(pk=self.item.id),
            'quantity': self.quantity,
            'bag': self.empty_bag,
            'redirect_url': f'/products/{self.item.id}/'
        }
        response = self.client.post(f'/bag/add/{self.item.id}/', post_data)
        self.assertEqual(response.status_code, 302)
        updated_bag = self.client.session.get('bag')
        self.assertEqual(len(updated_bag), 1)

    def test_add_to_bag_view_updates_item_if_exists(self):
        """
        Test that the add_to_bag view increases the quantity of
        an item if the item is already in the bag
        """
        session = self.client.session
        session['bag'] = self.filled_bag
        session.save()
        post_data = {
            'product': Product.objects.get(pk=14),
            'quantity': 3,
            'redirect_url': '/products/14/'
        }
        response = self.client.post('/bag/add/14/', post_data)
        self.assertEqual(response.status_code, 302)
        updated_bag = self.client.session.get('bag')
        self.assertEqual(updated_bag['14'], 4)

    def test_adjust_bag_view(self):
        """
        Test that the add_to_bag view updates the quantity of
        an item if the item is already in the bag
        """
        session = self.client.session
        session['bag'] = self.filled_bag
        session.save()
        post_data = {
            'bag_item': get_object_or_404(Product, pk=14),
            'quantity': int(self.quantity + 1),
        }
        response = self.client.post('/bag/adjust/14/', post_data)
        self.assertEqual(response.status_code, 302)
        updated_bag = self.client.session.get('bag')
        self.assertEqual(updated_bag['14'], 2)

    def test_adjust_bag_view_removes_item_when_quantity_is_less_than_1(self):
        """
        Test that the add_to_bag view removes an item if the
        quantity is set to less than 1
        """
        session = self.client.session
        session['bag'] = self.filled_bag
        session.save()
        post_data = {
            'bag_item': get_object_or_404(Product, pk=14),
            'quantity': int(self.quantity - 1),
        }
        response = self.client.post('/bag/adjust/14/', post_data)
        self.assertEqual(response.status_code, 302)
        updated_bag = self.client.session.get('bag')
        self.assertEqual(len(updated_bag), 1)

    def test_remove_from_bag_view(self):
        """
        Test that the remove_from_bag view removes an item
        from the bag
        """
        session = self.client.session
        session['bag'] = self.filled_bag
        session.save()
        response = self.client.post('/bag/remove/14/')
        self.assertEqual(response.status_code, 200)
        updated_bag = self.client.session.get('bag')
        self.assertEqual(len(updated_bag), 1)

    def test_remove_from_bag_error(self):
        """
        Test that the remove from bag view returns an error
        if something goes wrong
        """
        response = self.client.post('/bag/remove/66/')
        self.assertEqual(response.status_code, 500)

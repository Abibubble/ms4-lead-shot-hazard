from django.test import TestCase
from django.shortcuts import reverse

from .models import Category, Product


class TestProduct(TestCase):

    fixtures = [
        'categories.json',
        'products.json',
    ]

    def test_products_get(self):
        product = Product.objects.get(id=11)
        resp = self.client.get(reverse('products'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, product.name)

    def test_views_contains_products_get(self):
        product = Product.objects.get(id=11)
        resp = self.client.get(reverse('products'))
        self.assertContains(resp, product.name)

    def test_product_search_post(self):
        resp = self.client.get(
            '/products/?', {'q': 'tee'})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['search_term'], 'tee')

    def test_categories_get(self):
        product = Product.objects.get(id=11)
        resp = self.client.get(reverse('products'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, product.category)

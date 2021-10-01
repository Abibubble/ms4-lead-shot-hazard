from django.test import TestCase
from django.shortcuts import reverse

from .models import Category, Product


class TestProductViews(TestCase):
    """
    Test that the product views work as expected
    """

    fixtures = [
        'categories.json',
        'products.json',
    ]

    # Test that the products page URL exists
    def test_the_products_page_url_exists(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)

    # Test that the products page is accessible via name
    def test_the_products_url_is_accessible_by_name(self):
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)

    # Test that the products page uses the correct template
    def test_products_view_uses_correct_template(self):
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, template_name="products/products.html")

    # Test that a product can be retrieved
    def test_products(self):
        product = Product.objects.get(id=11)
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, product.name)

    # Test that the search bar returns what is expected
    def test_product_search_functionality(self):
        response = self.client.get(
            '/products/?', {'q': 'tee'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['search_term'], 'tee')

    # Test that the category sort feature works as expected
    def test_categories(self):
        product = Product.objects.get(id=11)
        category = Category.objects.get(pk=2)
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(product.category, category)
        self.assertContains(response, product.category)

    # Test that a product detail can be retrieved
    def test_product_detail(self):
        product = Product.objects.get(id=11)
        response = self.client.get(reverse('products'))
        self.assertContains(response, product.name)

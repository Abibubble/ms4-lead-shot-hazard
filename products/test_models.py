from django.test import TestCase

from .models import Category, Product


class TestProductModels(TestCase):
    """
    Test that the products work as expected
    """

    fixtures = [
        'categories.json',
        'products.json',
    ]

    # Test that the product name is retrieved correctly
    def test_product_name(self):
        product = Product.objects.get(pk=6)
        self.assertEqual(product.name, 'Old No. 7 Ska Band')
        self.assertNotEqual(product.name, 'Test name')
        self.assertEqual(str(product), product.name)

    # Test that the product description is retrieved correctly
    def test_product_description(self):
        product = Product.objects.get(pk=6)
        self.assertEqual(
            product.description, "Knock-off whiskey tee, because, why the hell not! Includes 'Hacky Sack? Let's Have A Rebellion' high-quality download in MP3, FLAC and more."
        )
        self.assertNotEqual(product.description, 'test if not equal')

    # Test whether a product has sizes or not
    def test_product_has_sizes(self):
        product_sizes = Product.objects.get(pk=6)
        product_no_sizes = Product.objects.get(pk=11)
        self.assertEqual(product_sizes.has_sizes, True)
        self.assertNotEqual(product_sizes.has_sizes, False)
        self.assertEqual(product_no_sizes.has_sizes, False)
        self.assertNotEqual(product_no_sizes.has_sizes, True)


class TestCategoryModels(TestCase):
    """
    Test that the categories work as expected
    """

    fixtures = [
        'categories.json',
    ]

    # Test that the category name and friendly name are retrieved correctly
    def test_category_name(self):
        category = Category.objects.get(pk=2)
        self.assertEqual(category.name, 'music')
        self.assertNotEqual(category.name, 'test')
        self.assertEqual(str(category), category.name)

    def test_category_friendly_name(self):
        category = Category.objects.get(pk=2)
        self.assertEqual(category.friendly_name, 'Music')
        self.assertNotEqual(category.friendly_name, 'Test Category')
        self.assertEqual(
            Category.get_friendly_name(category), category.friendly_name)

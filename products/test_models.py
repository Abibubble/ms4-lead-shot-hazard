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

    def test_product_name(self):
        """
        Test that the product name is retrieved correctly
        """
        product = Product.objects.get(pk=6)
        self.assertEqual(product.name, 'Old No. 7 Ska Band')
        self.assertNotEqual(product.name, 'Test name')
        self.assertEqual(str(product), product.name)

    def test_product_description(self):
        """
        Test that the product description is retrieved correctly
        """
        product = Product.objects.get(pk=6)
        self.assertEqual(
            product.description, "Knock-off whiskey tee, because, why the hell not! Includes 'Hacky Sack? Let's Have A Rebellion' high-quality download in MP3, FLAC and more." # noqa
        )
        self.assertNotEqual(product.description, 'test if not equal')

    def test_product_has_sizes(self):
        """
        Test whether a product has sizes or not
        """
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

    def test_category_name(self):
        """
        Test that the category name is retrieved correctly
        """
        category = Category.objects.get(pk=2)
        self.assertEqual(category.name, 'music')
        self.assertNotEqual(category.name, 'test')
        self.assertEqual(str(category), category.name)

    def test_category_friendly_name(self):
        """
        Test that the category friendly name is retrieved correctly
        """
        category = Category.objects.get(pk=2)
        self.assertEqual(category.friendly_name, 'Music')
        self.assertNotEqual(category.friendly_name, 'Test Category')
        self.assertEqual(
            Category.get_friendly_name(category), category.friendly_name)

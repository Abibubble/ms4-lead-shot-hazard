from django.test import TestCase

from .models import Category, Product


class TestProductModels(TestCase):

    fixtures = [
        'categories.json',
        'products.json',
    ]

    def test_product_name(self):
        product = Product.objects.get(pk=6)
        self.assertEqual(product.name, 'Old No. 7 Ska Band')

    def test_product_description(self):
        product = Product.objects.get(pk=6)
        self.assertEqual(
            product.description, "Knock-off whiskey tee, because, why the hell not! Includes 'Hacky Sack? Let's Have A Rebellion' high-quality download in MP3, FLAC and more."
        )

    def test_product_has_sizes(self):
        product = Product.objects.get(pk=6)
        self.assertEqual(product.has_sizes, True)


class TestCategoryModels(TestCase):

    fixtures = [
        'categories.json',
    ]

    def test_category_name(self):
        category = Category.objects.get(pk=2)
        self.assertEqual(category.name, 'music')
        self.assertEqual(category.friendly_name, 'Music')

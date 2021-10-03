from django.test import TestCase, RequestFactory
from django.shortcuts import reverse
from django.contrib.messages import get_messages
from django.contrib.auth.models import User
from django.http import HttpRequest

from .models import Category, Product
from .forms import ProductForm
from .views import add_product


class TestProductViews(TestCase):
    """
    Test that the product views work as expected
    """

    fixtures = [
        'categories.json',
        'products.json',
    ]

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            username='testuser', email='test@test.com', password='te12345st')

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
            response, template_name='products/products.html')

    # Test that a product can be retrieved
    def test_products(self):
        products = Product.objects.all()
        for product in products:
            response = self.client.get(reverse('products'))
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, product.pk)

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

    # Test that the product detail page URL exists
    def test_the_product_detail_page_url_exists(self):
        response = self.client.get('/products/11/')
        self.assertEqual(response.status_code, 200)

    # Test that the sort function works
    def test_sort_name_functionality(self):
        category_name = 'music'
        sort_array = ['name', 'category']
        for sort in sort_array:
            direction = 'desc'
            current_sorting = f'{sort}_{direction}'
            response = self.client.get(
                f'/products/?category={category_name}'
                f'&sort={sort}&direction={direction}')
            self.assertEqual(current_sorting, f'{sort}_desc')
            self.assertEqual(response.status_code, 200)

    # Test that the search bar returns what is expected
    def test_product_search_functionality(self):
        response = self.client.get(
            '/products/?', {'q': 'tee'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['search_term'], 'tee')

    # Test that the search error message display correctly
    def test_search_error_messages_output(self):
        response = self.client.get(
            '/products/?', {'q': ''})
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].tags, 'error')
        self.assertEqual(
            str(messages[0]), "You didn't enter any search criteria!")
        self.assertEqual(response.status_code, 302)

    # Test the add_product view doesn't allow non-superusers to access the page
    def test_add_product_for_regular_users_view(self):
        self.client.login(
            username='testuser', email='test@test.com', password='te12345st')
        response = self.client.get('/products/add/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].tags, 'error')
        self.assertEqual(
            str(messages[0]), 'Sorry, only store owners can do that.')
        self.assertEqual(response.status_code, 302)

    # Test that the add_product page works for superuser
    def test_the_add_product_page_works_for_superuser(self):
        my_admin = User.objects.create_superuser(
            username='testadmin', email='test@example.com',
            password='password')
        self.client.login(
            username=my_admin.username, email=my_admin.email,
            password='password')
        response = self.client.get('/products/add/')
        self.assertTemplateUsed(
            response, template_name='products/add_product.html')

    # Test that the superuser can add a valid product
    def test_superuser_can_add_valid_product(self):
        my_admin = User.objects.create_superuser(
            username='testadmin', email='test@example.com',
            password='password')
        self.client.login(
            username=my_admin.username, email=my_admin.email,
            password='password')
        data = {
            'category': '1',
            'sku': '',
            'name': 'test',
            'description': 'test description',
            'has_sizes': 'false',
            'has_audio': 'false',
            'audio': '',
            'price': '2.99',
            'image_url': '',
            'image': ''}
        self.client.post('/products/add/', data)
        response = self.client.get('/products/add/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].tags, 'success')
        self.assertEqual(
            str(messages[0]), 'Successfully added product.')

    # Test that the superuser cannot add an invalid product
    def test_superuser_cannot_add_invalid_product(self):
        my_admin = User.objects.create_superuser(
            username='testadmin', email='test@example.com',
            password='password')
        self.client.login(
            username=my_admin.username, email=my_admin.email,
            password='password')
        data = {
            'category': '1',
            'sku': '',
            'name': '',
            'description': 'test description',
            'has_sizes': 'false',
            'has_audio': 'false',
            'audio': '',
            'price': '2.99',
            'image_url': '',
            'image': ''}
        self.client.post('/products/add/', data)
        response = self.client.post('/products/add/', data)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].tags, 'error')
        self.assertEqual(
            str(messages[0]),
            'Failed to add product. Please check that the form is valid.')

    # Test the edit_product view doesn't allow
    # non-superusers to access the page
    def test_edit_product_for_regular_users_view(self):
        self.client.logout()
        self.client.login(
            username='testuser', email='test@test.com', password='te12345st')
        products = Product.objects.all()
        for product in products:
            response = self.client.get(f'/products/edit/{product.pk}/')
            messages = list(get_messages(response.wsgi_request))
            self.assertEqual(messages[0].tags, 'error')
            self.assertEqual(
                str(messages[0]), 'Sorry, only store owners can do that.')
            self.assertEqual(response.status_code, 302)

    # Test that the edit_product page works for superuser
    def test_the_edit_product_page_works_for_superuser(self):
        my_admin = User.objects.create_superuser(
            username='testadmin', email='test@example.com',
            password='password')
        self.client.login(
            username=my_admin.username, email=my_admin.email,
            password='password')
        products = Product.objects.all()
        for product in products:
            response = self.client.get(f'/products/edit/{product.pk}/')
            self.assertEqual(response.status_code, 200)

    # Test that the superuser can edit a valid product
    def test_superuser_can_edit_valid_product(self):
        my_admin = User.objects.create_superuser(
            username='testadmin', email='test@example.com',
            password='password')
        self.client.login(
            username=my_admin.username, email=my_admin.email,
            password='password')
        data = {
            'category': '1',
            'sku': '',
            'name': 'test',
            'description': 'test description',
            'has_sizes': 'false',
            'has_audio': 'false',
            'audio': '',
            'price': '2.99',
            'image_url': '',
            'image': ''}
        products = Product.objects.all()
        for product in products:
            product.name = 'test'
            self.client.post(f'/products/edit/{product.pk}/', data)
            response = self.client.get(f'/products/edit/{product.pk}/')
            messages = list(get_messages(response.wsgi_request))
            self.assertEqual(messages[0].tags, 'success')
            self.assertEqual(
                str(messages[0]), f'Successfully updated {product.name}.')

    # Test that the superuser cannot edit an invalid product
    def test_superuser_cannot_edit_invalid_product(self):
        my_admin = User.objects.create_superuser(
            username='testadmin', email='test@example.com',
            password='password')
        self.client.login(
            username=my_admin.username, email=my_admin.email,
            password='password')
        data = {
            'category': '1',
            'sku': '',
            'name': 'test',
            'description': 'test description',
            'has_sizes': 'false',
            'has_audio': 'false',
            'audio': '',
            'price': '2.99',
            'image_url': '',
            'image': ''}
        products = Product.objects.all()
        for product in products:
            product.description = ''
            response = self.client.post(
                f'/products/edit/{product.pk}/', data, product.description)
            messages = list(get_messages(response.wsgi_request))
            self.assertEqual(messages[0].tags, 'error')
            self.assertEqual(
                str(messages[0]),
                f'Failed to update {product.name}. Please check that the form is valid.')

    # Test the delete_product view doesn't allow
    # non-superusers to access the page
    def test_delete_product_for_regular_users_view(self):
        self.client.logout()
        self.client.login(
            username='testuser', email='test@test.com', password='te12345st')
        products = Product.objects.all()
        for product in products:
            response = self.client.get(f'/products/delete/{product.pk}/')
            messages = list(get_messages(response.wsgi_request))
            self.assertEqual(messages[0].tags, 'error')
            self.assertEqual(
                str(messages[0]), 'Sorry, only store owners can do that.')
            self.assertEqual(response.status_code, 302)

    # Test that the delete_product page works for superuser
    def test_the_delete_product_page_works_for_superuser(self):
        my_admin = User.objects.create_superuser(
            username='testadmin', email='test@example.com',
            password='password')
        self.client.login(
            username=my_admin.username, email=my_admin.email,
            password='password')
        products = Product.objects.all()
        for product in products:
            response = self.client.get(f'/products/delete/{product.pk}/')
            self.assertEqual(response.status_code, 302)

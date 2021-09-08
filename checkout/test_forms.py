from django.test import TestCase
from .forms import OrderForm


class TestOrderForm(TestCase):

    def test_full_name_is_required(self):
        # Submit form without a name filled in
        form = OrderForm({
            'full_name': '',
            'email': 'test@example.com',
            'phone_number': '09876543212',
            'country': 'gb',
            'town_or_city': 'test',
            'street_address1': 'test',
        })
        # Form should not be valid
        self.assertFalse(form.is_valid())
        # Find is there's a 'full_name' key in the dictionary of errors
        self.assertIn('full_name', form.errors.keys())
        # Check that the error message is correct
        self.assertEqual(
            form.errors['full_name'][0], 'This field is required.')

    def test_email_is_required(self):
        # Submit form without an email address filled in
        form = OrderForm({
            'full_name': 'tester',
            'email': '',
            'phone_number': '09876543212',
            'country': 'gb',
            'town_or_city': 'test',
            'street_address1': 'test',
        })
        # Form should not be valid
        self.assertFalse(form.is_valid())
        # Find is there's an 'email' key in the dictionary of errors
        self.assertIn('email', form.errors.keys())
        # Check that the error message is correct
        self.assertEqual(
            form.errors['email'][0], 'This field is required.')

    def test_phone_number_is_required(self):
        # Submit form without a phone number filled in
        form = OrderForm({
            'full_name': 'tester',
            'email': 'test@example.com',
            'phone_number': '',
            'country': 'gb',
            'town_or_city': 'test',
            'street_address1': 'test',
        })
        # Form should not be valid
        self.assertFalse(form.is_valid())
        # Find is there's a 'phone_number' key in the dictionary of errors
        self.assertIn('phone_number', form.errors.keys())
        # Check that the error message is correct
        self.assertEqual(
            form.errors['phone_number'][0], 'This field is required.')

    def test_country_is_required(self):
        # Submit form without a country filled in
        form = OrderForm({
            'full_name': 'tester',
            'email': 'test@example.com',
            'phone_number': '09876543212',
            'country': '',
            'town_or_city': 'test',
            'street_address1': 'test',
        })
        # Form should not be valid
        self.assertFalse(form.is_valid())
        # Find is there's a 'country' key in the dictionary of errors
        self.assertIn('country', form.errors.keys())
        # Check that the error message is correct
        self.assertEqual(
            form.errors['country'][0], 'This field is required.')

    def test_town_or_city_is_required(self):
        # Submit form without a name filled in
        form = OrderForm({
            'full_name': 'tester',
            'email': 'test@example.com',
            'phone_number': '09876543212',
            'country': 'gb',
            'town_or_city': '',
            'street_address1': 'test',
        })
        # Form should not be valid
        self.assertFalse(form.is_valid())
        # Find is there's a 'town_or_city' key in the dictionary of errors
        self.assertIn('town_or_city', form.errors.keys())
        # Check that the error message is correct
        self.assertEqual(
            form.errors['town_or_city'][0], 'This field is required.')

    def test_street_address1_is_required(self):
        # Submit form without a name filled in
        form = OrderForm({
            'full_name': 'tester',
            'email': 'test@example.com',
            'phone_number': '09876543212',
            'country': 'gb',
            'town_or_city': 'test',
            'street_address1': '',
        })
        # Form should not be valid
        self.assertFalse(form.is_valid())
        # Find is there's a 'street_address1' key in the dictionary of errors
        self.assertIn('street_address1', form.errors.keys())
        # Check that the error message is correct
        self.assertEqual(
            form.errors['street_address1'][0], 'This field is required.')

    def test_fields_are_correct_in_meta_class(self):
        form = OrderForm()
        self.assertEqual(form.Meta.fields, (
            'full_name', 'email', 'phone_number', 'country', 'postcode',
            'town_or_city', 'street_address1', 'street_address2', 'county',
        ))

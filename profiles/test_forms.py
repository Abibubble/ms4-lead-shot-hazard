from django.test import TestCase

from .forms import UserProfileForm


class TestUserProfileForm(TestCase):
    """
    Test the UserProfileForm works as expected
    """

    # Test that none of the form fields are required in the user profile
    def test_user_profile_form_fields_not_required(self):
        user_data = {
            'default_phone_number': '',
            'default_street_address1': '',
            'default_street_address2': '',
            'default_town_or_city': '',
            'default_postcode': '',
            'default_county': '',
            'default_country': ''
        }
        form = UserProfileForm(data=user_data)
        self.assertTrue(form.is_valid())
        self.assertFalse(form.errors)

    # Test that the user field is excluded in the profile UserProfileForm
    def test_user_profile_form_metaclass(self):
        form = UserProfileForm()
        self.assertEqual(form.Meta.exclude, ('user',))

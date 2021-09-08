from django.test import TestCase
from django.shortcuts import reverse


class TestViews(TestCase):

    def test_checkout_page(self):
        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 200)

    # def test_checkout_success_page(self):
    #     response = self.client.get('/checkout_success')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(
    #         response, 'templates/checkout/checkout_success.html')

from django.test import TestCase
from rest_framework.test import APIClient
from .models import MenuItem

class MenuAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        MenuItem.objects.create(title="Greek Salad", price="12.50", inventory=10)

    def test_menu_list_returns_200(self):
        response = self.client.get("/restaurant/menu/")
        self.assertEqual(response.status_code, 200)

    def test_menu_list_contains_created_item(self):
        response = self.client.get("/restaurant/menu/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Greek Salad")

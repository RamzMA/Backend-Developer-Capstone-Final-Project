from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer
from django.contrib.auth.models import User

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='james', password='james2012')
        self.client.force_authenticate(user=self.user)

        self.item1 = MenuItem.objects.create(title="Salad", price=10, inventory = 5)
        self.item2 = MenuItem.objects.create(title="Greek Salad", price=12, inventory = 8)

    def test_getall(self):
        url = '/menu/' 
        response = self.client.get(url)
        
        menu_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
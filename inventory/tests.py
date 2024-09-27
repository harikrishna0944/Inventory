from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from .models import Item

class ItemAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.item = Item.objects.create(name='Test Item', description='Test description', quantity=10)
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    def test_create_item(self):
        response = self.client.post('/api/items/', {'name': 'New Item', 'description': 'New description', 'quantity': 5})
        self.assertEqual(response.status_code, 201)
    
    def test_read_item(self):
        response = self.client.get(f'/api/items/{self.item.id}/')
        self.assertEqual(response.status_code, 200)

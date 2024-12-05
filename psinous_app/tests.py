from rest_framework.test import APIClient
from django.test import TestCase

class MemberTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_member_view(self):
        response = self.client.get('/api/member/')
        self.assertEqual(response.status_code, 200)
        print(response.json())

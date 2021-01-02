import json
import unittest
from project.tests.base import BaseTestCase


class TestUserService(BaseTestCase):
    """
        Users Service Test
    """
    def test_users(self):
        """
            Ensure the /hello route behaves as expected
        """
        response = self.client.get('/users/hello')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('hi you!', data['message'])
        self.assertIn('success', data['status'])

if __name__ == '__main__':
    unittest.main() 
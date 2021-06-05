import json
import unittest
from project.tests.base import BaseTestCase
from project.api.models import User
from project import db
# import logging

class TestUserService(BaseTestCase):

    """Tests for the Users Service."""

    def test_users(self):
        f"""Ensure the /ping route behaves correctly"""
        # print(self,flush=True)
        # log= logging.getLogger( f"{self.client}" )
        response = self.client.get('/users/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong!', data['message'])
        self.assertIn('success', data['status'])

    def test_add_user(self):
        """Ensure a new user can be added to the database."""

        with self.client:
            response = self.client.post('/users',
                data = json.dumps({
                    'username' : 'rishabh',
                    'email': 'rishabh103@gmail.com',
                    'password':'tomorrow123'
                }),
                content_type = 'application/json'
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertIn('rishabh103@gmail.com was added!', data['message'])
            self.assertIn('success', data['status'])
    
    def test_single_user(self):
        """Ensure get single user behaves correctly."""
        user = User(username='michael', email='michael@mherman.org',password='tomorrow123')
        db.session.add(user)
        db.session.commit()
        with self.client:
            response = self.client.get(f'/users/{user.id}')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertIn('michael', data['data']['username'])
            self.assertIn('michael@mherman.org', data['data']['email'])
            self.assertIn('success', data['status'])


if __name__ == '__main__':
    unittest.main()

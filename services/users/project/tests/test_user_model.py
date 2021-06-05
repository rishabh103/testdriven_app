import unittest
from project import db
from project.api.models import User
from project.tests.base import BaseTestCase
from sqlalchemy.exc import IntegrityError
import json,datetime,jwt
from flask import current_app
from project.tests.utils import add_user

class TestUserModel(BaseTestCase):
    def test_add_user(self):


        user = User(
            username='justatest',
            email='test@test.com',
            password='tomorrow123',
        )
        db.session.add(user)
        db.session.commit()
        self.assertTrue(user.id)
        self.assertEqual(user.username, 'justatest')
        self.assertEqual(user.email, 'test@test.com')
        self.assertTrue(user.active)

    def test_add_user_duplicate_username(self):


        user = User(
            username='justatest',
            email='test@test.com',
            password='tomorrow123',
        )
        db.session.add(user)
        db.session.commit()
        duplicate_user = User(
            username='justatest',
            email='test@test2.com',
            password='tomorrow123',
        )
        db.session.add(duplicate_user)
        self.assertRaises(IntegrityError, db.session.commit)
    
    def test_add_user_duplicate_email(self):
        user = User(
        username='justatest',
        email='test@test.com',
        password='tomorrow123',
        )
        db.session.add(user)
        db.session.commit()
        duplicate_user = User(
        username='justanothertest',
        email='test@test.com',
        password='tomorrow123',
        )
        db.session.add(duplicate_user)
        self.assertRaises(IntegrityError, db.session.commit)

    def test_to_json(self):
        user = User(
        username='justatest',
        email='test@test.com',
        password='tomorrow123',
        )
        db.session.add(user)
        db.session.commit()
        self.assertTrue(isinstance(user.to_json(), dict))

    def test_encode_auth_token(self):
        
        user = add_user('justatest', 'test@test.com', 'test')
        auth_token = user.encode_auth_token(user.id)
        self.assertTrue(isinstance(auth_token, str))
        
    
    def test_decode_auth_token(self):
        user = add_user('justatest', 'test@test.com', 'test')
        auth_token = user.encode_auth_token(user.id)
        self.assertTrue(isinstance(auth_token, str))
        self.assertEqual(user.decode_auth_token(auth_token), user.id)



if __name__ == '__main__':
    unittest.main()

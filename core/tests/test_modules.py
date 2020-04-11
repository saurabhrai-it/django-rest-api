from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Tests user is created with successful email"""
        email = "saurabhrai.it@hotmail.com"
        password = "testPass"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.password, password)

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = "saurabhrai.it@HOTMAIL.COM"
        user = get_user_model().objects.create_user(email, 'test@123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):             # this test would fail if it doesnt returns a ValueError
            get_user_model().objects.create_user(None, '23423')

    def test_create_new_super_user(self):
        """Test creating a new super user"""
        user = get_user_model().objects.create_superuser('test@temp.com','123456')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
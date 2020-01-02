from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = "test@gmail.com"
        password = 'Testpassword123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        """Test new user email is normalized"""
        email = "TEST@GMAIL.com"
        user = get_user_model().objects.create_user(email, 'test123')

        name, domain = email.split('@')
        self.assertEqual(user.email, f'{name}@{domain.lower()}')

    def test_new_user_invalid_email(self):
        """Test new user with no email raised error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')


    def test_creating_a_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            "test@gmail.com",
            'Testpassword123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
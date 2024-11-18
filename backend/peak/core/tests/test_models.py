"""
Test for models.
"""

from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    """Model Tets"""
    def test_create_user_with_email_success(self):
        email = 'mail@example.com'
        password = 'passexample123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_superuser(self):
        user = get_user_model().objects.create_superuser(email='email@example.com', password='pasword123')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    # TODO: extend tests e.g.:
    # - required email/pw input
    # - normalize email address
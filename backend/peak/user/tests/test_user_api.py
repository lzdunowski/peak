from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse('user:create')

# Create Mock user
# def _create_user(**params):
#   return get_user_model().objects.create_user(**params)


class PublicUserApiTests(TestCase):
    """Test public features of user API."""

    def setUp(self):
        self.client = APIClient()

    # Check if user sucessfuly created
    def test_create_user_success(self):
        # https://www.django-rest-framework.org/api-guide/testing/#api-test-cases
        "Test to check if creates user correclty."
        payload = {
            'email': 'test@example.com',
            'password': 'passpass123',
            'name': 'User name',
        }
        # Post data
        res = self.client.post(CREATE_USER_URL, payload)

        # AssertEqual that status code create response
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        # Check if password is not in response data
        self.assertNotIn(payload['password'], res.data)

        # Check if user is not superuser
        user = get_user_model().objects.get(email=payload['email'])
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    # TODO extend tests:
        # self.assertTrue(user.check_password(payload['password']))
        # self.assertNotIn('password', res.data)

    # def test_user_with_email_exists_error(self):
    #     "Test error returned when user already exists"
    #     payload = {
    #         'email': 'test@mail.com',
    #         'password': 'randompw123142',
    #         'name': 'Test name',
    #     }
    #     _create_user(payload['name'], payload['email'], payload['password'])
    #     user = _create_user(**payload)
    #     res = self.client.post(CREATE_USER_URL, payload)
    #     self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    # def test_password_to_short_error(self):
    #     """Test error message when password is too short"""
    #     payload = {
    #         'email' : 'test@mail.com',
    #         'password': 'pw',
    #         'name': 'Test name',
    #     }
    #     res = self.client.post(CREATE_USER_URL, payload)
    #     self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
    #     user_exists = get_user_model().objects.filter(
    #         email=payload['email']
    #     ).exists()
    #     self.assertFalse(user_exists)

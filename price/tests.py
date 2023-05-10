from django.test import TestCase
import os

from django.urls import reverse

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django

django.setup()
from rest_framework import status, response

from rest_framework.test import APITestCase, APIClient, APIRequestFactory

from config import settings

from price.models import CustomUser, Product
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from rest_framework.test import force_authenticate

from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient


class CustomUserCreateTestCase(APITestCase):
    def setUp(self) -> None:
        #############################################################################
        self.client = APIClient()
        self.client.login(user__email='andreymazo@mail.ru', password='qwert123asd')

        self.token = Token.objects.get(user__email='andreymazo@mail.ru')
        self.client = APIClient()

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_product_create_existed(self):
        response = self.client.post(
            reverse('price:product_create'),

            {'product_name': 'WWander',
             'user': 1,
             'category': 1,
             'product_description': 'Wondeful things',
             'price_value': 10
             }
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )


class CustomUserCreateTestCaseNewUser(APITestCase):
    def setUp(self) -> None:
        self.user = CustomUser(
            email='test@12.ru',
            seller=True,
        )

        self.user.set_password('qwert123asd')
        self.user.save()
        self.token = Token.objects.create(user=self.user)
        print('self.token.key', self.token.key)
        print(self.user.seller)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')

    def test_product_create(self):
        url = reverse('price:product_create')
        print(self.user.pk)  # 107
        data = {'user': self.user.pk,
                'product_name': 'WWander',
                'category': 1,
                'product_description': 'Wondeful things',
                'price_value': 10}
        response = self.client.post(
            # response = factory.post(
            url, data, format='json'
        )

        print('response.status_code', response.status_code)
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )


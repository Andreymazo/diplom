from django.test import TestCase
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django

django.setup()
from rest_framework import status, response

from rest_framework.test import APITestCase, APIClient, APIRequestFactory

from config import settings

from price.models import CustomUser
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from rest_framework.test import force_authenticate

factory = APIRequestFactory()
user = CustomUser.objects.get(email='andreymazo@mail.ru')

request = factory.post('/product_list/', {"user_id": 1,
                                          "product_name": "WWander",
                                          "category_id": 1,
                                          "product_description": "Wondeful things",
                                          "price_value": 10}, format='json')
print(response.Response.status_code)


#
class CustomUserCreateTestCase(APITestCase):
    def test_create(self):
        self.request = factory.post(
        "/product_list/",
        {"user_id": 1,
         "product_name": "WWander",
         "category_id": 1,
         "product_description": "Wondeful things",
         "price_value": 10}
    )
        print('self.response.status_code', response.Response.status_code)
        self.assertEquals(
        response.Response.status_code,
        status.HTTP_200_OK
    )

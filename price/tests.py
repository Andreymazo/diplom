from django.test import TestCase
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django

django.setup()
from rest_framework import status

from rest_framework.test import APITestCase, APIClient

from config import settings

from price.models import CustomUser
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

class CustomUserCreateTestCase(APITestCase):
    # https: // github.com / ilyachch / django - rest - framework - rusdoc / blob / master / api - guide / testing.md?ysclid = lhfe0laxo4627154828
    # from rest_framework.test import force_authenticate
    #
    # factory = APIRequestFactory()
    # user = User.objects.get(username='olivia')
    # view = AccountDetail.as_view()
    #
    # # Make an authenticated request to the view...
    # request = factory.get('/accounts/django-superstars/')
    # force_authenticate(request, user=user)
    # response = view(request)

    # user = User.objects.get(username='olivia')
    # request = factory.get('/accounts/django-superstars/')
    # force_authenticate(request, user=user, token=user.auth_token)

    def setUp(self) -> None:
        ##########################################
        self.user = CustomUser.objects.get(email='andreymazo@mail.ru')
        client = APIClient()
        client.force_authenticate(user=self.user)



        # Include an appropriate `Authorization:` header on all requests.
        # print('user__email', self.user.pk)
        # token = Token.objects.get(user_id=self.user.pk)
        # client = APIClient()
        # client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        # client.force_authenticate(user=None)
        ##################################################################
        self.user = CustomUser(
            email='andreymazo@mail.ru',
        )
        self.user.set_password('qwert123asd')
        # self.user.save()
        response = self.client.post(
            # "/api/token/",
            "rest-auth/login/",
            {'email': 'andreymazo@mail.ru', 'password': 'qwert123asd', 'is_active': 'True'},##, 'id': 4, 'is_superuser': False, 'is_staff': False
            # content_type="application/json"
        )
        #
        self.access_token = response.json().get('access')
        print(response.json().get('access'))
        # self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    # client = APIClient()
    # client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
    # response = client.get('/api/vehicles/')

    # client = RequestsClient()
    #
    # # Obtain a CSRF token.
    # response = client.get('http://testserver/homepage/')
    # assert response.status_code == 200
    # csrftoken = response.cookies['csrftoken']

    # # Interact with the API.
    # response = client.post('http://testserver/organisations/', json={
    #     'name': 'MegaCorp',
    #     'status': 'active'
    # }, headers={'X-CSRFToken': csrftoken})
    # assert response.status_code == 200

    def test_create(self):
        response = self.client.post(
            "/product_list/",
            {"user_id": 1,
            "product_name": "WWander",
            "category_id" : 1,
            "product_description": "Wondeful things",
            "price_value": 10}
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

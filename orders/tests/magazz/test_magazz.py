import json
import pytest
from rest_framework.test import APIClient
import os
from magazz.models import User
from dotenv import load_dotenv
import random

load_dotenv()







class TestApi:

    def __init__(self, client):
        self.client = client
        self.token_list = []
        self.id_list = []
        self.USER_INFO = {'first_name': 'Ivan',
                          'last_name': 'Test',
                          'email': 'test@test.com',
                          'password': 'qweUU78sq',
                          'company': 'company',
                          'position': 'manager'

                          }

    "Тест регистрации, подтверждения почты и входа в систему"
    def test_user_register(self):
        """
        Регистрация
        """
        response = self.client.post('/api/v1/user/register',
                               data=self.USER_INFO)
        r = response.json()
        assert response.status_code == 200
        assert r['Status'] is True
        """
        Подтверждение почты
        """

        x = open(os.getenv('path_file'))
        data = json.load(x)
        token_email = data['tok']
        response = self.client.post('/api/v1/user/register/confirm',
                               data={'email': 'test@test.com',
                                     'token': token_email})
        x.close()
        assert response.status_code == 200
        user_obj = User.objects.filter(email='test@test.com').values()
        for i in user_obj:
            assert i['is_active'] is True
        """
        Вход в систему
        """
        response = self.client.post('/api/v1/user/login',
                               data={'email': self.USER_INFO['email'],
                                     'password': self.USER_INFO['password']})
        r = response.json()
        self.token_list.append(r['Token'])
        with open(os.getenv('path_file'), 'w') as s:
            json.dump({'token': r['Token']}, s)
        assert response.status_code == 200
        assert r['Status'] is True
        assert len(r['Token']) > 0

    """Получение данных о пользователя"""
    def test_accoun_details_get(self):
        response = self.client.get('/api/v1/user/details',
                                   headers={'Authorization': f'Token { self.token_list[0]}'})
        r = response.json()
        self.id_list.append(r['id'])
        assert response.status_code == 200
        assert r['company'] == self.USER_INFO["company"] and \
               r['email'] == self.USER_INFO["email"] and \
               r['first_name'] == self.USER_INFO["first_name"] and \
               r['last_name'] == self.USER_INFO["last_name"]

        """Будет ли ошибка при неверном токене"""
        response = self.client.get('/api/v1/user/details',
                                   headers={'Authorization': f'Token {random.uniform(0, 20)}'})
        r = response.json()

        assert response.status_code == 401

    """Редактирование данных пользователя"""
    def test_accoun_details_post(self):
        new_name = random.randint(1, 100)
        new_password = 'asfgdbxcberh54546532462hbncb'
        response = self.client.post('/api/v1/user/details',
                                    headers={'Authorization': f'Token {self.token_list[0]}'},
                                    data={'first_name': str(new_name),
                                          'password': new_password}
                                    )
        r = response.json()

        assert response.status_code == 200
        assert r['Status'] is True and \
               r['request.data']['first_name'] == str(new_name) and \
               r['request.data']['password'] == new_password


    """Тест Shop"""
    def test_shop(self):
        """Создаем магазин"""
        shop_name = 'test'
        response = self.client.post('/api/v1/shops/',
                                    headers={'Authorization': f'Token {self.token_list[0]}'},
                                    data={'name': shop_name,
                                          'user': self.id_list[0]
                                          }
                                    )
        r = response.json()

        assert response.status_code == 201
        assert r['name'] == shop_name and\
               r['user'] == self.id_list[0]

        """Проверяем что тип пользователя сменился на Shop"""

        user_type = User.objects.filter(id=self.id_list[0])
        for i in user_type:
            assert i.type == 'shop'

        """Проверяем наличее магазина в выборке"""
        response_2 = self.client.get('/api/v1/shops/',
                                    headers={'Authorization': f'Token {self.token_list[0]}'})

        r_2 = response_2.json()
        assert int(r_2['count']) > 0
        assert r_2['results'][0]['name'] == shop_name
        """Проверяем фильтрацию"""
        response_3 = self.client.get(f'/api/v1/shops/{r["id"]}/',
                                   headers={'Authorization': f'Token {self.token_list[0]}'})

        r_3 = response_3.json()

        assert r_3['id'] == r["id"] and\
               r_3['name'] == r["name"] and\
               r_3['state'] is True




    """Просмотр и добавление категории"""
    def test_categories(self):

        """Добовляем новую категорию"""

        new_category = 'Ноутбуки'
        response_2 = self.client.post('/api/v1/categories/',
                                      headers={'Authorization': f'Token {self.token_list[0]}'},
                                      data={'name': new_category})
        r = response_2.json()
        assert response_2.status_code == 201
        assert r['name'] == new_category

        """Проверяем новую категорию в выборке"""

        response = self.client.get('/api/v1/categories/',
                                   headers={'Authorization': f'Token {self.token_list[0]}'})

        r = response.json()
        assert response.status_code == 200
        for i in r['results']:
            assert new_category in i.values()

    def test_partner_update(self):
        """Загружаем данные с ссылки"""
        url = 'https://raw.githubusercontent.com/swan-007/test/main/shop2.yaml'
        response = self.client.post('/api/v1/partner/update',
                                    headers={'Authorization': f'Token {self.token_list[0]}'},
                                    data={'url': url, })
        r = response.json()

        assert r['Status'] is True





@pytest.fixture
def client():
    return APIClient()


@pytest.mark.django_db
def test_action(client):
    obj = TestApi(client)
    obj.test_user_register()
    obj.test_accoun_details_get()
    obj.test_accoun_details_post()
    obj.test_shop()
    obj.test_categories()
    obj.test_partner_update()

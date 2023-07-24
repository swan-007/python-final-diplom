import requests
from pprint import pprint

from rest_framework.utils import json

# response = requests.get('http://127.0.0.1:8000/products',
#                         headers={'Authorization': 'Token 27b576e1bc18012d8773878558490fecb07c6b67'}
#                         )
"Регистрация"
# response = requests.post('http://127.0.0.1:8000/api/v1/user/register',
#                           data={'first_name': 'Ivan',
#                                'last_name': 'Ivanov',
#                                'email': 'legendyazii@gmail.com',
#                                'password': 'qweUU78sq',
#                                'company': 'company_1',
#                                'position': 'manager'})
#
# r = response.json()
# pprint(r)


"Подтверждение почты"
token_email = 'c427f77759de'
token_ses = '6f8328f597e33813b0d1ca50fe9e25e34c6646f2'
# response = requests.post('http://127.0.0.1:8000/api/v1/user/details',
#                          headers={'Authorization': f'Token {token_ses}'},
#                          data={'first_name': 'FDAe',
#                                'password': 'fdfdfwe45rt5rgbadfy'})
#
#
#
# r = response.json()
# pprint(r)
# "Авторизация"
# response = requests.post('http://127.0.0.1:8000/api/v1/user/login',
#                           data={
#                               'email': 'superlebedew@gmail.com',
#                               'password': 'dsdafdgcdgxfhxgdg'
#                               })
#
# r = response.json()
# pprint(r)
# # new_pass = dsdafdgcdgxfhxgdg
# token_ses = '6f8328f597e33813b0d1ca50fe9e25e34c6646f2'
# new_ = '6f8328f597e33813b0d1ca50fe9e25e34c6646f2'
# test = '1'
# response = requests.get('http://127.0.0.1:8000/api/v1/order',
#                         headers={'Authorization': f'Token {token_ses}'},
#                         data={'items': json.dumps([{'id': 1, 'quantity': 1, 'product_info': 1}])}
#
#                           )
#
# r = response.json()
# pprint(r)

response = requests.post('http://127.0.0.1:8000/api/v1/shops/',
                         headers={'Authorization': f'Token {token_ses}'},
                         data={'name': '7858test',
                               'user': '19',
                               }
                        )

r = response.json()
pprint(r)








# def test_user(client, headers):
#     resource = client.post('/user/register',
#                            data={ 'first_name': 'Ivan',
#                                   'last_name': 'Ivanov',
#                                   'email': 'legendyazii@gmail.com',
#                                   'password': 'qweUU78sq',
#                                   'company': 'company_1',
#                                   'position': 'manager'})
#     r = resource.json()
#     assert r["Status"] is True

# response = requests.get('http://127.0.0.1:8000/api/v1/user/details',
#                           headers={'Authorization': f'Token 6f8328f597e33813b0d1ca50fe9e25e34c6646f2'})
# r = response.json()
# pprint(r)
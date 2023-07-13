import requests
from pprint import pprint

from rest_framework.utils import json

# response = requests.get('http://127.0.0.1:8000/products',
#                         headers={'Authorization': 'Token 27b576e1bc18012d8773878558490fecb07c6b67'}
#                         )
"Регистрация"
# response = requests.post('http://127.0.0.1:8000/api/v1/user/register',
#                          data={'first_name': 'Sergey',
#                                   'last_name': 'Leb',
#                                   'email': 'superlebedew@gmail.com',
#                                   'password': 'qweUU78sq',
#                                   'company': 'CC',
#                                   'position': 'pos'})
#
# r = response.json()
# pprint(r)


"Подтверждение почты"
# token_email = 'c427f77759de'
# response = requests.post('http://127.0.0.1:8000/api/v1/user/register/confirm',
#                         data={
#                               'email': 'superlebedew@gmail.com',
#                               'token': token_email
#                               })
#
# r = response.json()
# pprint(r)
"Авторизация"
# response = requests.post('http://127.0.0.1:8000/api/v1/user/login',
#                           data={
#                               'email': 'superlebedew@gmail.com',
#                               'password': 'dsdafdgcdgxfhxgdg'
#                               })
#
# r = response.json()
# pprint(r)
# new_pass = dsdafdgcdgxfhxgdg
token_ses = '6f8328f597e33813b0d1ca50fe9e25e34c6646f2'
new_ = '6f8328f597e33813b0d1ca50fe9e25e34c6646f2'
test = '1'
# response = requests.get('http://127.0.0.1:8000/api/v1/order',
#                         headers={'Authorization': f'Token {token_ses}'},
#                         data={'items': json.dumps([{'id': 1, 'quantity': 1, 'product_info': 1}])}
#
#                           )
#
# r = response.json()
# pprint(r)

response = requests.post('http://127.0.0.1:8000/api/v1/order',
                        headers={'Authorization': f'Token {token_ses}'},
                        data={'id': 1, 'contact': 1}

                          )

r = response.json()
pprint(r)
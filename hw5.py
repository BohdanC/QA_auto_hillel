from pprint import pprint

import requests

url = 'https://dummyjson.com/users?limit=100'

response = requests.get(url)
our_users = response.json()

users = our_users.get('users', [])

ages = [user['age'] for user in users if user.get('hair').get('color').lower() == 'brown' \
        and user['gender'].lower() == 'male']
avg_age = sum(ages)/len(ages)
print(f'Avg age is {round(avg_age, 2)}')

lsvl_users = [(user.get('firstName', '') + ' ' + user.get('lastName', '')+ ' ' + user.get('maidenName', '')) for user \
              in users if user.get('address').get('city') == 'Louisville']
print(f'Louisville citizens: {lsvl_users}')

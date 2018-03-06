import requests
import json, os
from bs4 import BeautifulSoup


class web():
    def __init__(self, username='', password=''):
        if username == '':
            with open(os.path.join('cred', 'login.json')) as f:
                login = json.load(f)
        else:
            login = {
                'username': username,
                'password': password
            }

        url = 'https://www.wanikani.com/login'

        self.session = requests.Session()
        r = self.session.get(url)

        soup = BeautifulSoup(r.text, 'html.parser')

        login_data = {
            'utf8': "✓",
            'authenticity_token': soup.find('input', {'name': 'authenticity_token'})['value'],
            'user[login]': 'patarapolw@gmail.com',
            'user[password]': '4114951gu3',
            'user[remember_me]': 0
        }
        self.session.post(url, data=login_data)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


if __name__ == '__main__':
    os.chdir('../..')

    with web() as w:
        result = w.session.get('https://www.wanikani.com/dashboard')
        print(result.text)

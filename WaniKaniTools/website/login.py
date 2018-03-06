from selenium import webdriver
import requests
import json, os
from bs4 import BeautifulSoup


class Webdriver:
    def __init__(self, username='', password=''):
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        self.driver = webdriver.Firefox(firefox_options=options)
        site = 'https://www.wanikani.com/login'
        self.driver.get(site)

        if username == '':
            with open(os.path.join('cred', 'login.json')) as f:
                login = json.load(f)
        else:
            login = {
                'username': username,
                'password': password
            }

        self.driver.find_element_by_id("user_login").send_keys(login['username'])
        self.driver.find_element_by_id("user_password").send_keys(login['password'])
        self.driver.find_element_by_class_name("button").click()

    def logout(self):
        self.driver.quit()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.quit()


class Requests:
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
            'user[login]': login['username'],
            'user[password]': login['password'],
            'user[remember_me]': 0
        }
        self.session.post(url, data=login_data)


if __name__ == '__main__':
    os.chdir('../..')

    result = Requests().session.get('https://community.wanikani.com')
    print(result.text)

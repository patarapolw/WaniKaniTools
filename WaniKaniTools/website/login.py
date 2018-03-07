from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import json, os
import requests
from bs4 import BeautifulSoup
try:
    from requests_html import HTMLSession
except ImportError:
    pass


class Webdriver:
    def __init__(self, username='', password=''):
        try:
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            self.driver = webdriver.Chrome(chrome_options=options)
        except (FileNotFoundError, WebDriverException):
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


class RequestsHtml:
    def __init__(self, username='', password=''):
        if username == '':
            with open(os.path.join('cred', 'login.json')) as f:
                login = json.load(f)
        else:
            login = {
                'username': username,
                'password': password
            }

        community_login = 'https://community.wanikani.com/session/sso'
        wanikani_login = 'https://www.wanikani.com/login'

        self.session = HTMLSession()
        r = self.session.get(community_login)
        self.auth_token = r.html.find('input[@name="authenticity_token"]', first=True).attrs['value']

        self.login_data = {
            'utf8': "✓",
            'authenticity_token': self.auth_token,
            'user[login]': login['username'],
            'user[password]': login['password'],
            'user[remember_me]': 0
        }
        self.session.post(wanikani_login, data=self.login_data)


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

        community_login = 'https://community.wanikani.com/session/sso'
        wanikani_login = 'https://www.wanikani.com/login'

        self.session = requests.Session()
        r = self.session.get(community_login)
        self.auth_token = BeautifulSoup(r.text, 'html.parser')\
            .find('input', {'name': "authenticity_token"}).attrs['value']

        self.login_data = {
            'utf8': "✓",
            'authenticity_token': self.auth_token,
            'user[login]': login['username'],
            'user[password]': login['password'],
            'user[remember_me]': 0
        }
        self.session.post(wanikani_login, data=self.login_data)

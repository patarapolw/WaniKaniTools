from selenium import webdriver
import json, os
try:
    from requests_html import HTMLSession
except ImportError:
    import requests
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

        try:
            self.session = HTMLSession()
            r = self.session.get(url)
            auth_token = r.html.xpath('//input[@name="authenticity_token"]', first=True).attrs['value'],
        except NameError:
            self.session = requests.Session()
            r = self.session.get(url)
            auth_token = BeautifulSoup(r.text, 'html.parser').find('input', {'name': 'authenticity_token'})

        login_data = {
            'utf8': "✓",
            'authenticity_token': auth_token,
            'user[login]': login['username'],
            'user[password]': login['password'],
            'user[remember_me]': 0
        }
        self.session.post(url, data=login_data)


if __name__ == '__main__':
    os.chdir('../..')

    result = Requests().session.get('https://community.wanikani.com')
    print(result.text)

from selenium import webdriver
import requests
import json, os


class web():
    def __init__(self, username='', password=''):
        self.driver = webdriver.PhantomJS()
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

        cookie = self.driver.get_cookies()
        self.session = requests.Session()
        c = [self.session.cookies.set(c['name'], c['value']) for c in cookie]

    def logout(self):
        self.driver.quit()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.quit()


if __name__ == '__main__':
    os.chdir('..')

    with web() as w:
        result = w.session.get('https://www.wanikani.com/dashboard')
        print(result)
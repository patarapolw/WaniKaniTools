import os
import requests
from WaniKaniTools.website import login
from time import time

class discourse:
    def __init__(self, username='', password=''):
        with login.web(username, password) as w:
            w.driver.get('https://community.wanikani.com')
            w.driver.find_element_by_class_name('btn-primary').click()
            cookie = w.driver.get_cookies()
            self.session = requests.Session()
            c = [self.session.cookies.set(c['name'], c['value']) for c in cookie]

    def GET(self, end_point, params={}):
        url = 'https://community.wanikani.com/{}.json'.format(end_point)
        response = self.session.get(url, params=params)
        return response.text


if __name__ == '__main__':
    os.chdir('..')

    start = time()
    board = discourse()
    print('Time elasped: {} seconds'.format(time()-start)) # 56.1 seconds

    id = 10
    flag = ("all", "yearly", "quarterly", "monthly", "weekly", "daily")
    username = 'polv'
    end_point = (
        'categories', # Get a list of categories
        'c/{}'.format(id), # Get a list of topics in the specified category
        't/{}'.format(id), # Get a single topic
        'latest', # Get the latest topics
        'top', # Get the top topics
        'top/{}'.format(flag[0]), # Get the top topics filtered by specified flag
        'post/{}'.format(id), # Get a single post
        'users/{}'.format(username), # Get a single user by username
        'directory_items', # get a public list of users. Requires params: period, order
        'admin/users/list/{}'.format(flag), # returns a list of users
        'user_actions',

    )

    print(board.GET('users/polv'))

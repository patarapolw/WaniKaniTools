import os
from WaniKaniTools.website.login import Requests, Webdriver


class Discourse:
    def __init__(self, username='', password=''):
        # self.session = Requests(username, password).session
        # r = self.session.get('https://community.wanikani.com/login')
        # r.html.render()
        # SESSION_COOKIE = r.cookies
        # self.session.post('https://community.wanikani.com/login', cookies=SESSION_COOKIE)

        with Webdriver(username, password) as w:
            w.driver.get('https://community.wanikani.com/login')
            cookie = w.driver.get_cookies()
            self.session = Requests(username, password).session
            for c in cookie:
                self.session.cookies.set(c['name'], c['value'])

    def GET(self, end_point, params=None):
        if params is None:
            params = dict()
        url = 'https://community.wanikani.com/{}.json'.format(end_point)
        print(url)
        response = self.session.get(url, params=params)
        return response.text


if __name__ == '__main__':
    from time import time
    os.chdir('../..')

    start = time()
    board = Discourse()
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

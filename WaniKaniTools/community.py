import os

from WaniKaniTools.login import Requests


class Discourse:
    def __init__(self, username=None, password=''):
        if username is None:
            username = os.environ['USERNAME']
            password = os.environ['PASSWORD']

        self.session = Requests(username, password).session

    def GET(self, end_point, params=None):
        if params is None:
            params = dict()
        url = 'https://community.wanikani.com/{}.json'.format(end_point)
        response = self.session.get(url, params=params)
        return response.text

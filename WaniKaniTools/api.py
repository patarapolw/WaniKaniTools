import requests
import json
import os


class APIv1:
    def __init__(self, apiKey=None):
        if apiKey is None:
            apiKey = os.environ['API_V1']
        self.apiKey = apiKey

    def GET(self, resource, argument='', callback=None):
        r = requests.get("https://www.wanikani.com/api/user/{}/{}/{}".format(self.apiKey, resource, argument),
                           params={'callback': callback})
        return json.loads(r.text)


class APIv2:
    def __init__(self, apiKey=None):
        if apiKey is None:
            apiKey = os.environ['API_V2']
        HEADERS = {'Authorization': 'Bearer {}'.format(apiKey)}

        with requests.Session() as self.session:
            self.session.headers.update(HEADERS)

    def GET(self, resource, argument='', params=None):
        if params is None:
            params = dict()
        r = self.session.get("https://www.wanikani.com/api/v2/{}/{}".format(resource, argument), params=params)
        return json.loads(r.text)

    def GETurl(self, url):
        r = self.session.get(url)
        return json.loads(r.text)

import requests
import json
import os


class v1:
    def __init__(self, apiKey=None):
        if apiKey is None:
            with open(os.path.join('cred', 'key.json')) as f:
                apiKey = json.load(f)['v1']

        self.apiKey = apiKey

    def GET(self, resource, argument='', callback=None):
        r = requests.get("https://www.wanikani.com/api/user/{}/{}/{}".format(self.apiKey, resource, argument),
                           params={'callback': callback})
        return json.loads(r.text)


class v2:
    def __init__(self, apiKey=None):
        if apiKey is None:
            with open(os.path.join('cred', 'key.json')) as f:
                apiKey = json.load(f)['v2']

        HEADERS = {'Authorization': 'Bearer {}'.format(apiKey)}

        with requests.Session() as self.session:
            self.session.headers.update(HEADERS)

    def GET(self, resource, argument='', params={}):
        r = self.session.get("https://www.wanikani.com/api/v2/{}/{}".format(resource, argument), params=params)
        return json.loads(r.text)


if __name__ == '__main__':
    os.chdir('..')

    # api_v1
    resource = (
        'user-information',
        'study-queue',
        'level-progression',
        'srs-distribution',
        'recent-unlocks', # Argument is output limit in range 1-100. Default=10
        'critical-items', # Argument is percentage in range 0-100. Default=75
        'radicals', # Argument is level, comma-delimited. Default=all levels
        'kanji',
        'vocabulary'
    )
    api_v1 = v1()
    result = api_v1.GET(resource[2])['requested_information']


    # api_v2
    resource_v2 = (
        'user',
        'subjects', # Argument is id. Params are ids, types, slugs, levels, updated_after
        'assignments', # Argument is id. Params are ...
        'review_statistics',
        'study_materials',
        'summary',
        'reviews',
        'level_progressions',
        'resets'
    )
    api_v2 = v2()
    result = api_v2.GET(resource_v2[1])

    print(json.dumps(result, indent=4))

import os
import json


def load_credentials(path_to_credentials_json=None):
    if path_to_credentials_json is not None:
        with open(path_to_credentials_json)as f:
            cred = json.load(f)
    else:
        cred = {
            'login': {
                'username': input('Please input your username:'),
                'password': input('Please input your password:')
            },
            'api': {
                'v1': input('Please input your API v1:'),
                'v2': input('Please input your API v2:')
            }
        }
        with open('credentials.json', 'w') as f:
            json.dump(cred, f)

    os.environ['USERNAME'] = cred['login']['username']
    os.environ['PASSWORD'] = cred['login']['password']
    os.environ['API_V1'] = cred['api']['v1']
    os.environ['API_V2'] = cred['api']['v2']

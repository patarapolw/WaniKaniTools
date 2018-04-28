import os

from WaniKaniTools.credentials import load_credentials

if 'TRAVIS' not in os.environ:
    load_credentials('/Users/patarapolw/PycharmProjects/WaniKaniTools/credentials.json')

from setuptools import setup

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='WaniKaniTools',
    version='0.2.1',
    description='Working with WaniKani API, login, and Community.',
    long_description=long_description,
    url='https://github.com/patarapolw/WaniKaniTools',
    author='Pacharapol Withayasakpunt',
    author_email='patarapolw@gmail.com',
    keywords='WaniKani',
    packages=['WaniKaniTools'],
    python_requires='>=2.7',
    install_requires=['requests', 'bs4','requests-html', 'selenium'],
)

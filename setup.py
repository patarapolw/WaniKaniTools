from setuptools import setup

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='WaniKaniTools',
    version='0.3.0',
    description='Working with WaniKani API, login, and Community.',
    long_description=long_description,
    long_description_content_type='text/markdown',  # Optional (see note above)
    url='https://github.com/patarapolw/WaniKaniTools',
    author='Pacharapol Withayasakpunt',
    author_email='patarapolw@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Japanese',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities'
    ],
    keywords='WaniKani',
    packages=['WaniKaniTools'],
    package_data={
        'WaniKaniTools': ['database']
    },
    include_package_data=True,
    python_requires='>=2.7',
    install_requires=['requests', 'bs4', 'selenium'],
    extras_require={
        'tests': ['pytest', 'jaconv'],
        'full': ['requests-html']
    }
)

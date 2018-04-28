# How to use WaniKaniTools

[![Build Status](https://travis-ci.org/patarapolw/WaniKaniTools.svg?branch=master)](https://travis-ci.org/patarapolw/WaniKaniTools)
[![PyPI version shields.io](https://img.shields.io/pypi/v/WaniKaniTools.svg)](https://pypi.python.org/pypi/WaniKaniTools/)
[![PyPI license](https://img.shields.io/pypi/l/WaniKaniTools.svg)](https://pypi.python.org/pypi/WaniKaniTools/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/WaniKaniTools.svg)](https://pypi.python.org/pypi/WaniKaniTools/)
[![PyPI status](https://img.shields.io/pypi/status/WaniKaniTools.svg)](https://pypi.python.org/pypi/WaniKaniTOols/)

The following operations are supported by WaniKaniTools

* API v1 wrapper
* API v2 wrapper, and support for pagination
* Web login, and community login using `requests`
* Web login using `Chrome / Firefox` and able to both `execute_script()` and `click()` buttons accordingly

Sample working scripts are in `example/`. See also `tests/`.

## Installation

`pip install WaniKaniTools`

## Using API v1

```python
from WaniKaniTools import api

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
api_v1 = api.APIv1(put_your_api_v1_key_here)
result = api_v1.GET(resource[2])['requested_information'] # Output is Python dictionary
```

## Using API v2

### Basic operations

```python
from WaniKaniTools import api

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
api_v2 = api.APIv2(put_your_api_v2_key_here)
result = api_v2.GET(resource_v2[1]) # Output is Python dictionary
```

### Pagination

```python
from WaniKaniTools import api

api_v2 = api.APIv2(put_your_api_v2_key_here)
result = api_v2.GET('subjects')

while True:
    for data in result['data']:
        meaning_array = []
        for meaning in data["data"]["meanings"]:
            if meaning['primary']:
                meaning_array += [ meaning['meaning'] ]

        to_print = (
            data["id"],
            data["object"],
            data["data"]["characters"] if "characters" in data["data"] else data["data"]["character"],
            ', '.join(meaning_array),
            data["data"]["document_url"]
        )
        print(*to_print)

    next_url = result['pages']['next_url']

    if next_url is None:
        break

    result = api_v2.GETurl(next_url)
```

## Simulating web login

### Web login with requests

This is possible for most operations, including Discourse API, Burn Manager.

```python
from WaniKaniTools.login import Requests
s = Requests(your_username, your_password).session
```

### Web login and execute script

The operations supported here are the same as `selenium-webdriver`. Default uses Firefox's Geckodriver.

```python
from WaniKaniTools.login import Webdriver

with Webdriver(your_username, your_password) as w:
    w.driver.execute_script(put_your_javascript_here)
```

import pytest
import os

import tests
from WaniKaniTools.login import Requests, RequestsHtml, Webdriver


@pytest.mark.skipif('TRAVIS' in os.environ, reason='no credential specified')
def test_requests():
    result = Requests().session.get('https://www.wanikani.com')
    print(result.text)


@pytest.mark.skipif('TRAVIS' in os.environ, reason='no credential specified')
def test_requests_html():
    result = RequestsHtml().session.get('https://www.wanikani.com')
    result.html.render()
    print(result.text)


@pytest.mark.skipif('TRAVIS' in os.environ, reason='no credential specified')
def test_selenium():
    with Webdriver() as w:
        print(w.driver.page_source)


if __name__ == '__main__':
    # pytest.main([__file__, '-s'])
    test_requests_html()

from WaniKaniTools.website.login import Requests

if __name__ == '__main__':
    result = Requests().session.get('https://www.wanikani.com')
    print(result.text)

    # Webdriver class also available
    # from WaniKaniTools.website.login import Webdriver
    #
    # with Webdriver() as w:
    #     print(w.driver.page_source)

from WaniKaniTools.website.login import Requests

if __name__ == '__main__':
    import os
    os.chdir('..')

    result = Requests().session.get('https://www.wanikani.com')
    print(result.text)

    # Webdriver class also available

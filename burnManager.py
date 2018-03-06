from WaniKaniTools.website import login
from WaniKaniTools import chars2ids

if __name__ == '__main__':
    s = login.Requests().session
    for id in chars2ids(['人口']):
        s.put('https://www.wanikani.com/assignments/{}/resurrect'.format(id))

    # with login.Webdriver() as w:
    #     for id in chars2ids(['人口']):
    #         w.driver.execute_script(
    #             '$.ajax({url:"https://www.wanikani.com/assignments/{}/resurrect", method:"PUT"});'.format(id))

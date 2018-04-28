from WaniKaniTools.login import Requests
from WaniKaniTools.utils import chars2ids

if __name__ == '__main__':
    to_resurrect = ['人口']

    s = Requests().session
    for id, char in zip(chars2ids(to_resurrect), to_resurrect):
        data = {
            '_method': 'put',
            'authenticity_token': s.get('https://www.wanikani.com/vocabulary/{}'.format(char)).html\
                .find('meta[name=csrf-token]', first=True).attrs['content']
        }
        s.post('https://www.wanikani.com/assignments/{}/burn'.format(id), data=data)

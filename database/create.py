import os
import json

if __name__ == '__main__':
    os.chdir('..')
    from api import api

    api_v2 = api.v2()
    result = api_v2.GET('subjects')

    with open(os.path.join('database','id.txt'),'w') as fout:
        while True:
            for data in result['data']:
                meaning_array = []
                for meaning in data["data"]["meanings"]:
                    if meaning['primary']:
                        meaning_array += [ meaning['meaning'] ]

                to_print = (
                    str(data["id"]),
                    data["object"],
                    data["data"]["characters"] if "characters" in data["data"] else data["data"]["character"],
                    ', '.join(meaning_array),
                    data["data"]["document_url"]
                )
                print(*to_print)
                fout.write('\t'.join(str(x) for x in to_print) + '\n')

            next_url = result['pages']['next_url']

            if next_url is None:
                break

            result = json.loads(api_v2.session.get(next_url).text)
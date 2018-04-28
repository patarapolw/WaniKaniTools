from WaniKaniTools.api import APIv2
from WaniKaniTools.dir import database_path


def create_id_txt(path=database_path('id.txt')):
    api_v2 = APIv2()
    result = api_v2.GET('subjects')

    with open(path,'w') as fout:
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

            result = api_v2.GETurl(next_url)

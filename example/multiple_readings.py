import jaconv
from WaniKaniTools.api import APIv2


if __name__ == '__main__':
    api_v2 = APIv2()
    result = api_v2.GET('subjects', params={'types':'vocabulary'})

    # print(json.dumps(result, indent=4))
    while True:
        for data in result['data']:
            reading_array = set()
            for reading in data["data"]["readings"]:
                # if reading['primary']:
                    reading_array.add(jaconv.kata2hira(reading['reading']))

            if len(reading_array) == 1:
                continue

            meaning_array = []
            for meaning in data["data"]["meanings"]:
                if meaning['primary']:
                    meaning_array += [meaning['meaning']]

            to_print = (
                data["data"]["characters"] if "characters" in data["data"] else data["data"]["character"],
                ', '.join(reading_array),
                ', '.join(meaning_array)
            )
            print('\t'.join(to_print))

        next_url = result['pages']['next_url']

        if next_url is None:
            break

        result = api_v2.GETurl(next_url)
